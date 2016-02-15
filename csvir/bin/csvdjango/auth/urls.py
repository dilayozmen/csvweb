from django.conf.urls import include, url

urlpatterns = [
	url(r'^login/$','auth.views.login'),
	url(r'^authenticate/$','auth.views.authenticate'),
	url(r'^logout/$','auth.views.logout'),
]
