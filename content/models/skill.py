from django.db import models
from django.utils.translation import gettext_lazy as _

from content.models.base import BaseModel
from content.storages import OverwriteStorage


class Skill(BaseModel):
    PROFICIENCY = [
        (1, _('Novice')),
        (2, _('Beginner')),
        (3, _('Competent')),
        (4, _('Proficient')),
        (5, _('Expert')),
    ]

    name = models.CharField(verbose_name=_('Name'), max_length=255)
    icon = models.FileField(_("Icon"), upload_to='icons/', blank=True, null=True, storage=OverwriteStorage())
    proficiency = models.PositiveSmallIntegerField(
        _("Proficiency"),
        choices=PROFICIENCY,
        default=3,
    )
    category = models.ForeignKey(
        'SkillCategory',
        verbose_name=_("Category"),
        related_name='skills',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-proficiency', 'name']


class SkillCategory(BaseModel):
    name = models.CharField(_("Category Name"), max_length=100)
    icon = models.FileField(_("Icon"), upload_to='category_icons/', blank=True, null=True)
    order = models.PositiveSmallIntegerField(_("Order"), default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = _('Skill Categories')
