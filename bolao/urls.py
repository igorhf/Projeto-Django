from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^aposta/$', views.aposta, name='aposta'),
]
