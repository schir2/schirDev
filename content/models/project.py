from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from content.models.base import BaseModel


class Project(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), )
    skills = models.ManyToManyField('content.Skill', verbose_name=_('Skills'), related_name='projects')
    company = models.ForeignKey('Company', verbose_name=_('Company'), max_length=255, on_delete=models.SET_NULL,
                                null=True, related_name='projects')
    year = models.PositiveSmallIntegerField(verbose_name=_('Year'), default=timezone.now().year, )
    image = models.ImageField(verbose_name=_('Image'), upload_to='projects/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-year',)


