from django.contrib import admin

from blog.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'creator', 'created_at', 'edited_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'creator')
