from django.urls import path

from content.views.home_views import home_view

app_name = 'content'

urlpatterns = [
    path('', home_view, name='home'),
]
