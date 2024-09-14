from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from content.models.base import BaseModel


class Project(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), )
    tech_stacks = models.ManyToManyField('TechStack', verbose_name=_('Tech Stack'), related_name='projects')
    company = models.ForeignKey('Company', verbose_name=_('Company'), max_length=255, on_delete=models.SET_NULL,
                                null=True, related_name='projects')
    year = models.PositiveSmallIntegerField(verbose_name=_('Year'), default=timezone.now().year, )
    image = models.ImageField(verbose_name=_('Image'), upload_to='projects/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-year',)


class TechStack(BaseModel):
    PROFICIENCY = [
        (1, _('Novice')),
        (2, _('Beginner')),
        (3, _('Competent')),
        (4, _('Proficient')),
        (5, _('Expert')),
    ]

    name = models.CharField(verbose_name=_('Name'), max_length=255)
    icon = models.FileField(_("Icon"), upload_to='icons/', blank=True, null=True)
    proficiency = models.PositiveSmallIntegerField(
        _("Proficiency"),
        choices=PROFICIENCY,
        default=3,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
