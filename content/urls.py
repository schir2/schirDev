from django.urls import path
from django.urls.conf import include

from content.views import home_view, contact_message_form_view

app_name = 'content'

urlpatterns = [
    path('', home_view, name='home'),
    path('forms/', include([
        path('contact_message', contact_message_form_view, name='contact_message_form'),
    ]))
]
