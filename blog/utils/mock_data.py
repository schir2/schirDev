import logging
import random

from django.contrib.auth import get_user_model
from django.utils import timezone

from blog.factories import UserFactory, ArticleFactory, TopicFactory, TagFactory
from blog.models import Comment, ArticleInteraction, FeaturedArticle

logger = logging.getLogger(__name__)


def generate_mock_blog_data(num_users=100, num_articles=200, num_topics=10, num_tags=30):
    User = get_user_model()

    logger.info(
        f"Starting mock data generation: {num_users} users, {num_articles} articles, {num_topics} topics, {num_tags} tags")

    # Create users
    users = [UserFactory() for _ in range(num_users)]
    logger.debug(f"Created {num_users} users")

    # Create topics
    tech_topics = ['Python', 'Django', 'HTMX', 'JavaScript', 'Kubernetes', 'Docker', 'CI/CD', 'Cloud Computing',
                   'Machine Learning', 'Web Development']
    other_topics = ['Rock Climbing', 'Trail Running', 'Ultramarathon', 'Bouldering', 'Fitness']
    topics = [TopicFactory(name=topic) for topic in tech_topics + other_topics]
    logger.debug(f"Created {len(topics)} topics")

    # Create tags
    tech_tags = ['backend', 'frontend', 'devops', 'database', 'api', 'security', 'performance', 'testing', 'frameworks',
                 'libraries']
    other_tags = ['outdoor', 'gear', 'training', 'nutrition', 'competition', 'travel']
    tags = [TagFactory(name=tag) for tag in tech_tags + other_tags]
    logger.debug(f"Created {len(tags)} tags")

    # Create articles
    articles = []
    for i in range(num_articles):
        article = ArticleFactory(
            creator=random.choice(users),
            topic=random.choice(topics),
            created_at=timezone.now() - timezone.timedelta(days=random.randint(0, 365))
        )
        article.tags.set(random.sample(tags, k=random.randint(1, 5)))

        # Add comments
        comment_count = random.randint(0, 10)
        Comment.objects.bulk_create([
            Comment(
                article=article,
                creator=random.choice(users),
                content=f"This is a {'great' if random.random() > 0.2 else 'controversial'} article about {article.topic}!"
            ) for _ in range(comment_count)
        ])

        # Add interactions
        interaction_count = random.randint(10, 100)
        ArticleInteraction.objects.bulk_create([
            ArticleInteraction(
                article=article,
                creator=random.choice(users),
                interaction_type=random.choice(['like', 'dislike'])
            ) for _ in range(interaction_count)
        ])

        articles.append(article)

        if i % 50 == 0:
            logger.info(f"Created {i} articles")

    logger.info(f"Finished creating {num_articles} articles")

    # Create featured articles
    featured_articles = random.sample(articles, k=min(10, len(articles)))
    for article in featured_articles:
        FeaturedArticle.objects.create(
            article=article,
            featured_reason=random.choice([
                FeaturedArticle.FeaturedReason.EDITOR_CHOICE,
                FeaturedArticle.FeaturedReason.STAFF_PICK,
                FeaturedArticle.FeaturedReason.TOPIC_HIGHLIGHT,
                FeaturedArticle.FeaturedReason.POPULAR_ARTICLE
            ])
        )
    logger.debug(f"Featured {len(featured_articles)} articles")

    # Update popularity scores
    for article in articles:
        article.calculate_popularity_score()
    logger.debug("Updated popularity scores for all articles")

    logger.info(
        f"Mock data generation complete: {num_users} users, {num_articles} articles, {len(topics)} topics, and {len(tags)} tags")
    logger.info(f"Featured {len(featured_articles)} articles")