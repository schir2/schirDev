from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('content.urls', namespace='content')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('arcus/', include('arcus.urls', namespace='arcus')),
    path('tools/', include('tools.urls', namespace='tools')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('users/', include('django.contrib.auth.urls', )),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'schir.dev admin'
