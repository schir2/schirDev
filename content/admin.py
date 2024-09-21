from django.contrib import admin

from content.models import Page, Skill, Project, SkillCategory, Company
from blog.models.post import Post


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'creator', 'created_at', 'edited_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'creator')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'creator', 'created_at', 'edited_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'creator')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('proficiency', 'category')
    search_fields = ('name',)


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'get_skills', 'image', 'year')
    search_fields = ('name', 'company__name')
    list_filter = ('company', 'skills')

    def get_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])

    get_skills.short_description = 'Skills'
