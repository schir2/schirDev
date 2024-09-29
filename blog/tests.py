from unittest.mock import patch, Mock

from django.db import IntegrityError
from django.test import TestCase, RequestFactory
from django.utils import timezone
from django.utils.text import slugify

from blog.factories import create_article_with_interactions, UserFactory, ArticleFactory, TopicFactory, TagFactory
from blog.models import Article, InteractionType, ArticleInteraction, Comment, FeaturedArticle


class ArticleTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.topic = TopicFactory()
        cls.tag = TagFactory()
        cls.user1 = UserFactory()
        cls.user2 = UserFactory()

    def setUp(self):
        self.article = ArticleFactory(creator=self.user, topic=self.topic)
        self.article.tags.add(self.tag)
        self.request_factory = RequestFactory()

    def test_slug_is_generated(self):
        """Test that a slug is automatically generated when an article is created."""
        article = Article.objects.create(
            title="Test Article",
            content="Test content",
            topic=self.topic,
            creator=self.user1
        )
        expected_slug = slugify(article.title)
        self.assertEqual(article.slug, expected_slug)

    def test_slug_is_unique_for_different_titles(self):
        """Test that unique slugs are generated for different article titles."""
        article1 = Article.objects.create(
            title="Unique Title 1",
            content="Test content",
            topic=self.topic,
            creator=self.user1
        )
        article2 = Article.objects.create(
            title="Unique Title 2",
            content="Test content",
            topic=self.topic,
            creator=self.user1
        )
        self.assertNotEqual(article1.slug, article2.slug)

    def test_slug_is_unique_for_same_title_different_users(self):
        """Test that articles with the same title by different users get unique slugs."""
        article1 = Article.objects.create(
            title="Same Title",
            content="Test content",
            topic=self.topic,
            creator=self.user1
        )
        article2 = Article.objects.create(
            title="Same Title",
            content="Test content",
            topic=self.topic,
            creator=self.user2
        )
        # The second slug should be different, likely appending a UUID or a unique suffix
        self.assertNotEqual(article1.slug, article2.slug)

    def test_slug_appends_unique_suffix(self):
        """Test that when an article with a duplicate title is created, a unique suffix is added."""
        article1 = Article.objects.create(
            title="Test Article",
            content="Test content",
            topic=self.topic,
            creator=self.user1
        )
        article2 = Article.objects.create(
            title="Test Article",  # Same title as article1
            content="Different content",
            topic=self.topic,
            creator=self.user2
        )

        # The second article should have a slug with a UUID suffix or some unique addition
        expected_base_slug = slugify(article1.title)
        self.assertTrue(article2.slug.startswith(expected_base_slug))
        self.assertNotEqual(article1.slug, article2.slug)

    def test_slug_does_not_change_on_edit(self):
        """Test that the slug does not change if the title is unchanged during editing."""
        article = Article.objects.create(
            title="Test Article",
            content="Test content",
            topic=self.topic,
            creator=self.user1
        )
        original_slug = article.slug
        # Edit the content but not the title
        article.content = "Updated content"
        article.save()
        # The slug should remain the same
        self.assertEqual(article.slug, original_slug)

    def test_slug_changes_when_title_is_edited(self):
        """Test that the slug changes if the title is changed during editing."""
        article = Article.objects.create(
            title="Original Title",
            content="Test content",
            topic=self.topic,
            creator=self.user1
        )
        original_slug = article.slug
        # Update the title
        article.title = "Updated Title"
        article.save()
        # The slug should change to reflect the updated title
        updated_slug = slugify(article.title)
        self.assertNotEqual(article.slug, original_slug)
        self.assertEqual(article.slug, updated_slug)

    def test_article_creation(self):
        self.assertIsInstance(self.article, Article)
        self.assertEqual(self.article.creator, self.user)

    def test_article_with_interactions(self):
        article = create_article_with_interactions()
        self.assertEqual(article.comments.count(), 3)
        self.assertEqual(article.interactions.filter(interaction_type='like').count(), 5)
        self.assertEqual(article.interactions.filter(interaction_type='dislike').count(), 2)

    def test_increment_view_count(self):
        request = self.request_factory.get('fake-url')
        request.user = self.user
        initial_count = self.article.view_count
        self.article.increment_view_count(request)
        self.article.refresh_from_db()
        self.assertEqual(self.article.view_count, initial_count + 1)

        self.article.increment_view_count(request)
        self.article.refresh_from_db()
        self.assertEqual(self.article.view_count, initial_count + 1)

    @patch('django.utils.timezone.now')
    @patch('blog.models.Article.interactions')
    @patch('blog.models.Article.comments')
    def test_calculate_popularity_score(self, mock_comments, mock_interactions, mock_now):
        mock_now.return_value = timezone.make_aware(timezone.datetime(2023, 1, 1))

        article = ArticleFactory(
            created_at=timezone.make_aware(timezone.datetime(2022, 1, 1)),
            view_count=500
        )

        # Setup mocks
        mock_interactions.filter.return_value.count.return_value = 50
        mock_comments.count.return_value = 25

        with patch.object(Article, 'save') as mock_save:
            score = article.calculate_popularity_score()

            self.assertGreater(score, 0)
            self.assertLess(score, 1)
            mock_save.assert_called_once()
            self.assertEqual(article.popularity_score, score)

        # Verify that the mocks were called
        mock_interactions.filter.assert_called_once()
        mock_comments.count.assert_called_once()

    def test_likes_and_dislikes_properties(self):
        article = ArticleFactory()
        for _ in range(5):
            article.interactions.create(creator=UserFactory(), interaction_type=InteractionType.LIKE)
        for _ in range(3):
            article.interactions.create(creator=UserFactory(), interaction_type=InteractionType.DISLIKE)

        self.assertEqual(article.likes.count(), 5)
        self.assertEqual(article.dislikes.count(), 3)

    def test_is_featured_property(self):
        article = ArticleFactory()
        self.assertFalse(article.is_featured)

        # Create a FeaturedArticle instance for this article
        FeaturedArticle.objects.create(article=article)
        self.assertTrue(article.is_featured)

    def test_unique_together_constraint(self):
        article1 = ArticleFactory(creator=self.user, title="Test Article")
        with self.assertRaises(IntegrityError):
            ArticleFactory(creator=self.user, title="Test Article")

    def test_str_method(self):
        article = ArticleFactory(title="Test Article")
        self.assertEqual(str(article), "Test Article")

    def test_ordering(self):
        ArticleFactory(title="Old Article", created_at=timezone.now() - timezone.timedelta(days=2))
        ArticleFactory(title="New Article", created_at=timezone.now())
        articles = Article.objects.all()
        self.assertEqual(articles[0].title, "New Article")
        self.assertEqual(articles[1].title, "Old Article")
