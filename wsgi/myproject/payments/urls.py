__author__ = 'jonathan'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/', views.add, name='add'),
    url(r'^addPerson/', views.addPerson, name='addPerson'),
    url(r'^addPlace/', views.addPlace, name='addPlace'),
    url(r'^addTravel/', views.addTravel, name='addTravel'),


]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()