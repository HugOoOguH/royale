from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Royale.as_view(), name="royale"),
]