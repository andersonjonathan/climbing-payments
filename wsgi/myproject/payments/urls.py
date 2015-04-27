__author__ = 'jonathan'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^addPerson/', views.addPerson, name='addPerson'),
    url(r'^addPlace/', views.addPlace, name='addPlace'),
    url(r'^addTravel/', views.addTravel, name='addTravel'),
    url(r'^person/(?P<pk>[0-9]+)/(?P<did>[0-9]+)/', views.hasPayed, name='hasPayed'),
    url(r'^person/(?P<pk>[0-9]+)/', views.pay, name='pay'),
    url(r'^person/', views.PersonView.as_view(), name='person'),
    url(r'^login/', views.loginView, name='loginView'),
    url(r'^logout/', views.logout_view, name='logout_view'),

]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()