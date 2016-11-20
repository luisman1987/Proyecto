from django.conf.urls import include, url
from blogperros import views
from django.conf import settings
from django.conf.urls. static import static

urlpatterns = [
#url(r'^$', 'blogpersona.views.post_list'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
