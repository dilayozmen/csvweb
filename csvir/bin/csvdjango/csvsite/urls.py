from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^editcsv','csvsite.views.editcsv'),
    ]
