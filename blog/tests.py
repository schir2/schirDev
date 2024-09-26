from django.test import TestCase
from django.utils.text import slugify

from blog.models import ArticleCategory, Article
from users.models import User


class ArticleTestCase(TestCase):

    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')

        # Create a category for articles
        self.category = ArticleCategory.objects.create(name='Test Category', slug='test-category')

    def test_slug_is_generated(self):
        """Test that a slug is automatically generated when an article is created."""
        article = Article.objects.create(
            title="Test Article",
            content="Test content",
            category=self.category,
            creator=self.user1
        )
        expected_slug = slugify(article.title)
        self.assertEqual(article.slug, expected_slug)

    def test_slug_is_unique_for_different_titles(self):
        """Test that unique slugs are generated for different article titles."""
        article1 = Article.objects.create(
            title="Unique Title 1",
            content="Test content",
            category=self.category,
            creator=self.user1
        )
        article2 = Article.objects.create(
            title="Unique Title 2",
            content="Test content",
            category=self.category,
            creator=self.user1
        )
        self.assertNotEqual(article1.slug, article2.slug)

    def test_slug_is_unique_for_same_title_different_users(self):
        """Test that articles with the same title by different users get unique slugs."""
        article1 = Article.objects.create(
            title="Same Title",
            content="Test content",
            category=self.category,
            creator=self.user1
        )
        article2 = Article.objects.create(
            title="Same Title",
            content="Test content",
            category=self.category,
            creator=self.user2
        )
        # The second slug should be different, likely appending a UUID or a unique suffix
        self.assertNotEqual(article1.slug, article2.slug)

    def test_slug_appends_unique_suffix(self):
        """Test that when an article with a duplicate title is created, a unique suffix is added."""
        article1 = Article.objects.create(
            title="Test Article",
            content="Test content",
            category=self.category,
            creator=self.user1
        )
        article2 = Article.objects.create(
            title="Test Article",  # Same title as article1
            content="Different content",
            category=self.category,
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
            category=self.category,
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
            category=self.category,
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
