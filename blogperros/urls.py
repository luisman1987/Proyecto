from django.conf.urls import include, url
from blogperros import views
from django.conf import settings
from django.conf.urls. static import static

urlpatterns = [
    url(r'^$', 'blogperros.views.listado_perros'),
    url(r'^perro_detalle/(?P<pk>[0-9]+)/$', 'blogperros.views.detalle_perro'),
    url(r'^perro/nuevo/$', 'blogperros.views.perro_nuevo', name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', 'blogperros.views.perro_editar', name='editar'),

    url(r'^listado/personas/$', 'blogperros.views.listado_personas', name='listado'),
    url(r'^persona/detalle/(?P<pk>[0-9]+)/$', 'blogperros.views.detalle_persona'),
    url(r'^persona/nueva/$', 'blogperros.views.persona_nueva', name='post_new'),
    url(r'^editar/(?P<pk>[0-9]+)/edit/$', 'blogperros.views.editar_persona', name='post_edit'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
