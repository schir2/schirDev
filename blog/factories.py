# blog/factories.py

import factory
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from factory.django import DjangoModelFactory

from .models import Article, Topic, Tag, Comment, ArticleInteraction, ArticleSeries


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')


class TopicFactory(DjangoModelFactory):
    class Meta:
        model = Topic

    name = factory.Faker('word')
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker('sentence')


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker('word')
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))


class ArticleSeriesFactory(DjangoModelFactory):
    class Meta:
        model = ArticleSeries

    title = factory.Faker('sentence')
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    description = factory.Faker('paragraph')


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker('sentence')
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    content = factory.Faker('paragraph', nb_sentences=5)
    creator = factory.SubFactory(UserFactory)
    topic = factory.SubFactory(TopicFactory)
    is_published = True
    view_count = factory.Faker('random_int', min=0, max=1000)
    popularity_score = factory.Faker('pyfloat', left_digits=1, right_digits=2, positive=True, max_value=1)
    series = None
    series_sequence_number = None

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)
        else:
            self.tags.add(TagFactory())


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    article = factory.SubFactory(ArticleFactory)
    creator = factory.SubFactory(UserFactory)
    content = factory.Faker('paragraph')
    is_approved = True


class ArticleInteractionFactory(DjangoModelFactory):
    class Meta:
        model = ArticleInteraction

    article = factory.SubFactory(ArticleFactory)
    creator = factory.SubFactory(UserFactory)
    interaction_type = factory.Iterator(['like', 'dislike'])


# Helper function to create a full article with related objects
def create_article_with_interactions(num_comments=3, num_likes=5, num_dislikes=2):
    article = ArticleFactory()
    CommentFactory.create_batch(num_comments, article=article)
    ArticleInteractionFactory.create_batch(num_likes, article=article, interaction_type='like')
    ArticleInteractionFactory.create_batch(num_dislikes, article=article, interaction_type='dislike')
    return article
