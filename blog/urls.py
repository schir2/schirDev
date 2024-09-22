from django.urls import path
from django.urls.conf import include

from blog.views import article_list_view, article_detail_view, home_view

app_name = 'blog'

urlpatterns = [
    path('', home_view, name='home'),
    path('articles/', include([
        path('', article_list_view, name='article_list'),
        path('<int:pk>/', article_detail_view, name='article_detail'),
    ]))
]
