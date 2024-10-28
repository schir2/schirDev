import logging
import random

from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify

from blog.factories import UserFactory
from blog.models import Article, Topic, Tag, Comment, ArticleInteraction, FeaturedArticle

logger = logging.getLogger(__name__)


def generate_unique_slugs(names, existing_slugs=None):
    if existing_slugs is None:
        existing_slugs = set()
    unique_slugs = {}
    for name in names:
        base_slug = slugify(name)
        slug = base_slug
        counter = 1
        while slug in existing_slugs or slug in unique_slugs.values():
            slug = f"{base_slug}-{counter}"
            counter += 1
        unique_slugs[name] = slug
        existing_slugs.add(slug)
    return unique_slugs


@transaction.atomic
def generate_mock_blog_data(num_users=100, num_articles=200, num_topics=10, num_tags=30):
    logger.info(
        f"Starting mock data generation: {num_users} users, {num_articles} articles, {num_topics} topics, {num_tags} tags")

    # Create users
    users = UserFactory.create_batch(num_users)
    logger.info(f"Created {num_users} users")

    # Prepare topics
    tech_topics = ['Python', 'Django', 'HTMX', 'JavaScript', 'Kubernetes', 'Docker', 'Cloud Computing',
                   'Machine Learning', 'Web Development']
    other_topics = ['Rock Climbing', 'Trail Running', 'Ultramarathon', 'Bouldering', 'Fitness']
    all_topics = tech_topics + other_topics

    # Get existing topic slugs
    existing_topic_slugs = set(Topic.objects.values_list('slug', flat=True))
    topic_slugs = generate_unique_slugs(all_topics, existing_topic_slugs)

    # Bulk create topics
    topics = Topic.objects.bulk_create([
        Topic(name=name, slug=slug)
        for name, slug in topic_slugs.items()
    ])
    logger.info(f"Created {len(topics)} topics")

    # Prepare tags
    tech_tags = ['backend', 'frontend', 'devops', 'database', 'api', 'security', 'performance', 'testing', 'frameworks',
                 'libraries']
    other_tags = ['outdoor', 'gear', 'training', 'nutrition', 'competition', 'travel']
    all_tags = tech_tags + other_tags

    # Get existing tag slugs
    existing_tag_slugs = set(Tag.objects.values_list('slug', flat=True))
    tag_slugs = generate_unique_slugs(all_tags, existing_tag_slugs)

    # Bulk create tags
    tags = Tag.objects.bulk_create([
        Tag(name=name, slug=slug)
        for name, slug in tag_slugs.items()
    ])
    logger.info(f"Created {len(tags)} tags")

    # Generate rich content function (simplified for brevity)
    def generate_rich_content(topic_name):
        return f"<h1>{topic_name}</h1><p>This is a sample article about {topic_name}.</p>"

    # Prepare article data
    article_data = []
    for i in range(num_articles):
        topic = random.choice(topics)
        article_data.append({
            'creator': random.choice(users),
            'topic': topic,
            'created_at': timezone.now() - timezone.timedelta(days=random.randint(0, 365)),
            'title': f"Article about {topic.name} - {i}",
            'content': generate_rich_content(topic.name),
            'slug': slugify(f"Article about {topic.name} - {i}"),
            'image': f'blog/article_images/sample_image_{random.randint(1, 5)}.jpg'
        })

    # Bulk create articles
    articles = Article.objects.bulk_create([Article(**data) for data in article_data])
    logger.info(f"Created {len(articles)} articles with rich content and images")

    # Bulk create article-tag relationships
    article_tags = [
        Article.tags.through(article_id=article.id, tag_id=tag.id)
        for article in articles
        for tag in random.sample(tags, k=random.randint(1, 5))
    ]
    Article.tags.through.objects.bulk_create(article_tags)

    # Bulk create comments
    comments = [
        Comment(
            article=article,
            creator=random.choice(users),
            content=f"This is a {'great' if random.random() > 0.2 else 'controversial'} article about {article.topic}!"
        )
        for article in articles
        for _ in range(random.randint(0, 10))
    ]
    Comment.objects.bulk_create(comments)

    # Bulk create interactions
    interactions = [
        ArticleInteraction(
            article=article,
            creator=random.choice(users),
            interaction_type=random.choice(['like', 'dislike'])
        )
        for article in articles
        for _ in range(random.randint(10, 100))
    ]
    ArticleInteraction.objects.bulk_create(interactions)

    # Create featured articles
    featured_articles = random.sample(articles, k=min(10, len(articles)))
    FeaturedArticle.objects.bulk_create([
        FeaturedArticle(
            article=article,
            featured_reason=random.choice([
                FeaturedArticle.FeaturedReason.EDITOR_CHOICE,
                FeaturedArticle.FeaturedReason.STAFF_PICK,
                FeaturedArticle.FeaturedReason.TOPIC_HIGHLIGHT,
                FeaturedArticle.FeaturedReason.POPULAR_ARTICLE
            ])
        )
        for article in featured_articles
    ])
    logger.info(f"Featured {len(featured_articles)} articles")
    for article in articles:
        article.calculate_popularity_score()
    logger.info("Updated popularity scores for all articles")

    logger.info(
        f"Mock data generation complete: {num_users} users, {num_articles} articles, {len(topics)} topics, and {len(tags)} tags")