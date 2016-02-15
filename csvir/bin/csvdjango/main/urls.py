from django.conf.urls import include, url
from  . import views

urlpatterns = [
    url(r'^$','main.views.home'),
	url(r'^home/$','main.views.home'),
    ]
