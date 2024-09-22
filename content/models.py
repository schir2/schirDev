from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from content.storages import OverwriteStorage


class Company(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    url = models.URLField(verbose_name=_("URL"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = _('Companies')


class ContactMessage(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    email = models.EmailField(verbose_name=_('Email'))
    subject = models.CharField(verbose_name=_('Subject'), max_length=100)
    message = models.TextField(verbose_name=_('Message'))

    def __str__(self):
        return f'{self.name}, {self.email}, {self.subject}'

    class Meta:
        ordering = ('-created_at',)


class Page(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    content = models.TextField(verbose_name=_('Content'))
    show_on_homepage = models.BooleanField(verbose_name=_('Show on homepage'), default=False)
    show_in_navbar = models.BooleanField(verbose_name=_('Show on navigation'), default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Project(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), )
    skills = models.ManyToManyField('content.Skill', verbose_name=_('Skills'), related_name='projects')
    company = models.ForeignKey('Company', verbose_name=_('Company'), max_length=255, on_delete=models.SET_NULL,
                                null=True, related_name='projects', blank=True)
    year = models.PositiveSmallIntegerField(verbose_name=_('Year'), default=timezone.now().year, )
    image = models.ImageField(verbose_name=_('Image'), upload_to='projects/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-year',)


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
