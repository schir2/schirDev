from django.contrib import admin
from django.utils.html import format_html

from .models import Article, ArticleCategory, Comment, FeaturedArticle, ArticleInteraction
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'edited_at', 'creator', 'editor')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'is_published', 'popularity_score', 'created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('category', 'is_published', 'tags', 'created_at')
    search_fields = ('title', 'content', 'category__name', 'tags__name')
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['category', 'tags']
    ordering = ['-created_at']
    readonly_fields = ('image_preview', 'popularity_score', 'created_at', 'edited_at', 'creator', 'editor')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 200px;"/>', obj.image.url)
        return ""

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'created_at', 'edited_at', 'creator', 'editor')
    search_fields = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'content', 'is_approved', 'created_at', 'creator')
    list_filter = ('is_approved', 'created_at', 'article__title')
    search_fields = ('content', 'article__title', 'creator__username')
    ordering = ['-created_at']
    actions = ['approve_comments']
    readonly_fields = ('is_approved', 'created_at', 'edited_at', 'creator', 'editor')

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True, updater=request.user)

    approve_comments.short_description = "Approve selected comments"


@admin.register(FeaturedArticle)
class FeaturedArticleAdmin(admin.ModelAdmin):
    list_display = ('article', 'featured_reason', 'created_at', 'edited_at', 'creator', 'editor')
    search_fields = ('article__title', 'featured_reason')
    ordering = ['-created_at']
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')


@admin.register(ArticleInteraction)
class ArticleInteractionAdmin(admin.ModelAdmin):
    list_display = ('article', 'interaction_type', 'creator', 'created_at')
    list_filter = ('interaction_type', 'created_at', 'article__title')
    search_fields = ('article__title', 'creator__username', 'interaction_type')
    ordering = ['-created_at']
    readonly_fields = ('created_at', 'edited_at', 'creator', 'editor')
