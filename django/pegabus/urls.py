from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from pegabus import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


admin.autodiscover()
admin.site.site_header = 'PegaBus'
admin.site.site_title = 'Página administrativa'
admin.site.index_title = 'PegaBus'
