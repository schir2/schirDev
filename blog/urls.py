from django.urls import path
from django.urls.conf import include

from blog.views import article_list_view, article_detail_view, blog_index_view, article_create_view, tag_list_view, \
    tag_detail_view, tag_create_view, tag_edit_view, tag_delete_view, topic_list_view, topic_create_view, \
    topic_detail_view, topic_edit_view, topic_delete_view, article_like_count_view, article_dislike_count_view, \
    toggle_dislike_view, toggle_like_view

app_name = 'blog'

urlpatterns = [
    path('', blog_index_view, name='index'),
    path('articles/', include([
        path('', article_list_view, name='article_list'),
        path('create', article_create_view, name='article_create'),
        path('<str:slug>/',
             include([
                 path('', article_detail_view, name='article_detail'),
                 path('like_count', article_like_count_view, name='article_like_count'),
                 path('dislike_count', article_dislike_count_view, name='article_dislike_count'),
                 path('toggle-like/', toggle_like_view, name='toggle_like'),
                 path('toggle-dislike/', toggle_dislike_view, name='toggle_dislike'),

             ])
             ),
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
