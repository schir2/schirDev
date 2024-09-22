from django.urls import path
from django.urls.conf import include

from blog.views import article_list_view, article_detail_view, blog_index_view

app_name = 'blog'

urlpatterns = [
    path('', blog_index_view, name='index'),
    path('articles/', include([
        path('', article_list_view, name='article_list'),
        path('<int:pk>/', article_detail_view, name='article_detail'),
    ]))
]
