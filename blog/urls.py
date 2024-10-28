from django.urls import path
from django.urls.conf import include

from blog.views import article_list_view, article_detail_view, home_view, article_create_view, tag_list_view, \
    tag_detail_view, tag_create_view, tag_edit_view, tag_delete_view, topic_list_view, topic_create_view, \
    topic_detail_view, topic_edit_view, topic_delete_view, article_like_count_view, article_dislike_count_view, \
    toggle_dislike_view, toggle_like_view, article_archive_view, article_edit_view, article_view_count_view, \
    article_comments_view, article_add_comment_view, css_display_cheatsheet_view, theme_view, article_series_list_view, \
    article_series_detail_view, article_series_get_next_sequence_number_view

app_name = 'blog'

urlpatterns = [
    path('', home_view, name='index'),
    path('theme', theme_view, name='theme'),
    path('articles/', include([
        path('', article_list_view, name='article_list'),
        path('create', article_create_view, name='article_create'),
        path('<str:slug>/',
             include([
                 path('', article_detail_view, name='article_detail'),
                 path('edit', article_edit_view, name='article_edit'),
                 path('archive', article_archive_view, name='article_archive'),
                 path('like_count', article_like_count_view, name='article_like_count'),
                 path('dislike_count', article_dislike_count_view, name='article_dislike_count'),
                 path('toggle_like/', toggle_like_view, name='toggle_like'),
                 path('toggle_dislike/', toggle_dislike_view, name='toggle_dislike'),
                 path('view_count/', article_view_count_view, name='article_view_count'),
                 path('comments', article_comments_view, name='article_comments'),
                 path('add_comment', article_add_comment_view, name='article_add_comment')

             ])
             ),
        path('article_series/', include([
            path('', article_series_list_view, name='article_series_list'),
            path('<str:slug>/', include([
                path('', article_series_detail_view, name='article_series_detail'),
                path('get_next_sequence_number', article_series_get_next_sequence_number_view,
                     name='article_series_get_next_sequence_number')
            ]))
        ])),
        path('resources/', include([
            path('css_display_cheatsheet', css_display_cheatsheet_view, name='css_display_cheatsheet'),
        ])),
        path('tags/', include([
            path('', tag_list_view, name='tag_list'),
            path('create', tag_create_view, name='tag_create'),
            path('<str:slug>/', include([
                path('', tag_detail_view, name='tag_detail'),
                path('edit', tag_edit_view, name='tag_edit'),
                path('delete', tag_delete_view, name='tag_delete'),
            ]))
        ])),
        path('topics/', include([
            path('', topic_list_view, name='topic_list'),
            path('create', topic_create_view, name='topic_create'),
            path('<str:slug>/', include([
                path('', topic_detail_view, name='topic_detail'),
                path('edit', topic_edit_view, name='topic_edit'),
                path('delete', topic_delete_view, name='topic_delete'),
            ]))
        ]))
    ]))
]
