from django.db import models
from django.utils.translation import gettext_lazy as _

from content.models.base import BaseModel


class ContactMessage(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    email = models.EmailField(verbose_name=_('Email'))
    subject = models.CharField(verbose_name=_('Subject'), max_length=100)
    message = models.TextField(verbose_name=_('Message'))

    def __str__(self):
        return f'{self.name}, {self.email}, {self.subject}'

    class Meta:
        ordering = ('-created_at',)
