from django.conf.urls import include, url
from blogperros import views
from django.conf import settings
from django.conf.urls. static import static

urlpatterns = [
    url(r'^$', 'blogperros.views.listado_perros'),
    url(r'^post/(?P<pk>[0-9]+)/$', 'blogperros.views.detalle_perro'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
