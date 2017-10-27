from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^travels$', views.index),
    url(r'^travels/add$', views.add),
    url(r'^travels/create$', views.create),
    url(r'^travels/join/(?P<id>\d+)$', views.join),
    url(r'^travels/destination/(?P<id>\d+)$', views.destination),

]