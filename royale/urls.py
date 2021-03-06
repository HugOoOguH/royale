from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from main import urls as mainUrls
from django.conf import settings
from main.api import urls as apiUrls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(mainUrls, namespace="main")),
    url(r'^api/', include(apiUrls)),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}),
]
