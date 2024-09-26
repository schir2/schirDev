from django.contrib import admin

from .models import ArticleCategory, Comment, Tag, Article


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'edited_at', 'creator', 'editor')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'created_at', 'edited_at', 'creator', 'editor')
    list_filter = ('category', 'is_published', 'tags', 'created_at')
    search_fields = ('title', 'content', 'category__name', 'tags__name')
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['category', 'tags']
    ordering = ['-created_at']
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return '<img src="{}" style="max-width: 200px;"/>'.format(obj.image.url)
        return ""

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'edited_at', 'creator', 'editor')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'content', 'is_approved', 'created_at', 'creator')
    list_filter = ('is_approved', 'created_at', 'article__title')
    search_fields = ('content', 'article__title', 'creator__username')
    ordering = ['-created_at']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)

    approve_comments.short_description = "Approve selected comments"
