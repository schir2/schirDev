import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

from common.models import BaseModel


class Article(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    content = HTMLField(verbose_name=_('Content'), )
    topic = models.ForeignKey('blog.Topic', verbose_name=_('Topic'), related_name='articles',
                              on_delete=models.SET_NULL,
                              blank=True, null=True)
    tags = models.ManyToManyField('blog.Tag', verbose_name=_('Tags'), related_name='articles', blank=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='blog/article_images/', blank=True, null=True)
    is_published = models.BooleanField(_('Is published'), default=True)
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

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        unique_together = ('title', 'creator',)


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
    content = HTMLField(verbose_name=_('Content'), )
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
    featured_reason = models.TextField(blank=True, choices=FeaturedReason.choices, verbose_name=_('Reason for Featuring'))

    def __str__(self):
        return f'Featured article {self.article.title}'

    class Meta:
        verbose_name = _('Featured Article')
        verbose_name_plural = _('Featured Articles')
        ordering = ['-created_at']


class ArticleInteraction(BaseModel):
    class InteractionType(models.TextChoices):
        LIKE = 'like', 'Like'
        DISLIKE = 'dislike', 'Dislike'

    article = models.ForeignKey('Article', verbose_name=_('Article'), on_delete=models.CASCADE,
                                related_name='interactions')
    interaction_type = models.CharField(choices=InteractionType.choices, max_length=10)

    def __str__(self):
        return f'Interaction {self.creator.username} {self.interaction_type} {self.article.title}'

    class Meta:
        verbose_name = _('Interaction')
        verbose_name_plural = _('Interactions')
        ordering = ['-created_at']
