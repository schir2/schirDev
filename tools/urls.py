from django.urls import path

from tools import views
from tools.views import theme_view, css_display_cheatsheet_view

app_name = 'tools'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('retirement_calculator', views.retirement_calculator_view, name='retirement_calculator'),
    path('css_display_cheatsheet', css_display_cheatsheet_view, name='css_display_cheatsheet'),
    path('theme', theme_view, name='theme'),
]
