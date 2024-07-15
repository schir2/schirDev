from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Page(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    content = models.TextField(verbose_name=_('Content'))
    created_at = models.DateTimeField(verbose_name=_('Created At'), default=timezone.now)
    updated_at = models.DateTimeField(verbose_name=_('Uploaded At'), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_('Author'), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
