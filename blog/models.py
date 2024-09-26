from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Article(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    content = models.TextField(verbose_name=_('Content'), )
    category = models.ForeignKey('ArticleCategory', verbose_name=_('Category'), related_name='articles',
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)
    tags = models.ManyToManyField('blog.Tag', verbose_name=_('Tags'), related_name='articles', blank=True)
    is_published = models.BooleanField(_('Is published'), default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')


class ArticleCategory(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100, unique=True)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True, max_length=100)


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
