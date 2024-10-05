import uuid
from typing import Union

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.text import slugify, Truncator
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from common.models import BaseModel

User = get_user_model()


class InteractionType(models.TextChoices):
    LIKE = 'like', 'Like'
    DISLIKE = 'dislike', 'Dislike'


class Article(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    content = RichTextUploadingField(verbose_name=_('Content'), )
    topic = models.ForeignKey('blog.Topic', verbose_name=_('Topic'), related_name='articles',
                              on_delete=models.SET_NULL,
                              blank=True, null=True)
    tags = models.ManyToManyField('blog.Tag', verbose_name=_('Tags'), related_name='articles', blank=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='blog/article_images/', blank=True, null=True)
    is_published = models.BooleanField(_('Is published'), default=True)
    view_count = models.PositiveIntegerField(verbose_name=_('View count'), default=0)
    popularity_score = models.FloatField(verbose_name=_('Popularity Score'), default=0.0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        if not self.slug or not self.slug.startswith(base_slug):
            slug = base_slug
            if Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"  # Append UUID for uniqueness
            self.slug = slug
        super().save(*args, **kwargs)

    def increment_view_count(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        user_id = request.user.id if request.user.is_authenticated else None
        cache_key = f'article_view_{self.id}_{user_id or client_ip}'

        if not cache.get(cache_key):
            self.view_count = models.F('view_count') + 1
            self.save(update_fields=['view_count'])
            cache.set(cache_key, True, 60 * 60 * 24)

    def calculate_popularity_score(self):
        now = timezone.now()

        time_weight = 0.3
        view_weight = 0.4
        interaction_weight = 0.3

        time_diff = now - self.created_at
        time_factor = 1 / (1 + time_diff.days)

        view_factor = min(self.view_count / 1000, 1)

        like_count = self.interactions.filter(interaction_type=InteractionType.LIKE).count()
        comment_count = self.comments.count()
        interaction_factor = min((like_count + comment_count) / 100, 1)

        score = (
                time_weight * time_factor +
                view_weight * view_factor +
                interaction_weight * interaction_factor
        )

        self.popularity_score = score
        self.save(update_fields=['popularity_score'])

        return score

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        unique_together = ('title', 'creator',)

    @property
    def likes(self):
        return self.interactions.filter(interaction_type=InteractionType.LIKE)

    @property
    def dislikes(self):
        return self.interactions.filter(interaction_type=InteractionType.DISLIKE)

    @property
    def is_featured(self):
        return hasattr(self, 'featured')

    def user_has_liked(self, user: Union[User, None]) -> bool:
        """
        Check if the given user has liked this article.

        Args:
            user (User): The user to check for a like interaction.

        Returns:
            bool: True if the user has liked the article, False otherwise.

        Note:
            If the user is None (anonymous user), this will always return False.
        """
        if user is None or user.is_anonymous:
            return False
        return self.interactions.filter(creator=user, interaction_type='like').exists()

    def user_has_disliked(self, user: Union[User, None]) -> bool:
        """
        Check if the given user has disliked this article.

        Args:
            user (User): The user to check for a dislike interaction.

        Returns:
            bool: True if the user has disliked the article, False otherwise.

        Note:
            If the user is None (anonymous user), this will always return False.
        """
        if user is None or user.is_anonymous:
            return False
        return self.interactions.filter(creator=user, interaction_type='dislike').exists()

    # ... existing fields ...

    def safe_excerpt(self, words=30, char_limit=None):
        """
        Generate a safe, plain-text excerpt of the article content.

        Args:
            words (int): The number of words to include in the excerpt. Defaults to 30.
            char_limit (int, optional): The maximum number of characters for the excerpt.

        Returns:
            str: A plain-text excerpt of the article content.
        """
        plain_text = strip_tags(self.content)

        if char_limit:
            return Truncator(plain_text).chars(char_limit, truncate='...')
        else:
            return Truncator(plain_text).words(words, truncate='...')


class Topic(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100, unique=True)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True, max_length=100)
    description = models.TextField(verbose_name=_('Description'), blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    def __str__(self):
        return self.name


class Comment(BaseModel):
    article = models.ForeignKey(Article, verbose_name=_('Article'), related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(verbose_name=_('Content'), )
    is_approved = models.BooleanField(_('Is approved'), default=True)

    def __str__(self):
        return f'Comment by {self.creator} on {self.article.title}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class Tag(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100, unique=True)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True, max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class FeaturedArticle(BaseModel):
    class FeaturedReason(models.TextChoices):
        EDITOR_CHOICE = 'editor_choice', _("Editor's Choice")
        STAFF_PICK = 'staff_pick', _("Staff Pick")
        TOPIC_HIGHLIGHT = 'topic_highlight', _("Topic Highlight")
        POPULAR_ARTICLE = 'popular_article', _("Popular Article")

    article = models.OneToOneField('Article', verbose_name=_('Article'), on_delete=models.CASCADE,
                                   related_name='featured')
    featured_reason = models.TextField(blank=True, choices=FeaturedReason.choices,
                                       verbose_name=_('Reason for Featuring'))

    def __str__(self):
        return f'Featured article {self.article.title}'

    class Meta:
        verbose_name = _('Featured Article')
        verbose_name_plural = _('Featured Articles')
        ordering = ['-created_at']


class ArticleInteraction(BaseModel):
    article = models.ForeignKey('Article', verbose_name=_('Article'), on_delete=models.CASCADE,
                                related_name='interactions')
    interaction_type = models.CharField(choices=InteractionType.choices, max_length=10)

    def __str__(self):
        return f'Interaction {self.creator.username} {self.interaction_type} {self.article.title}'

    class Meta:
        verbose_name = _('Interaction')
        verbose_name_plural = _('Interactions')
        ordering = ['-created_at']
