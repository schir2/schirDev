from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from content.models.base import BaseModel

User = get_user_model()


class Post(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    content = models.TextField(verbose_name=_('Content'), )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
