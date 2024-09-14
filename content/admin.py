from django.contrib import admin

from content.models import Page, Post, TechStack, Project
from content.models.company import Company


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


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    list_filter = ('proficiency',)
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'get_tech_stacks', 'image', 'year')
    search_fields = ('name', 'company__name')
    list_filter = ('company', 'tech_stacks')

    def get_tech_stacks(self, obj):
        return ", ".join([tech.name for tech in obj.tech_stacks.all()])

    get_tech_stacks.short_description = 'Tech Stack'
