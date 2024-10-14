from django.urls import path
from tools import views

app_name = 'tools'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('retirement_calculator', views.retirement_calculator_view, name='retirement_calculator'),
]