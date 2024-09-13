from django.db import models
from django.utils.translation import gettext_lazy as _

from content.models.base import BaseModel


class Company(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    url = models.URLField(verbose_name=_("URL"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
