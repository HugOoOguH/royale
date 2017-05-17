from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^cards/$', views.CardList.as_view(), name="cards_list"),
	
]

urlpatterns = format_suffix_patterns(urlpatterns)