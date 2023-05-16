from django.urls import path
from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^clients/$', views.ClientsListView.as_view(), name='clients'),
    re_path(r'^clients/(?P<pk>\d+)$', views.ClientsDetailView.as_view(), name='user-detail'),
    re_path(r'^clients/create/$', views.ClientsCreate.as_view(), name='clients_create'),
    re_path(r'^clients/(?P<pk>\d+)/update/$', views.ClientsUpdate.as_view(), name='clients_update'),
    re_path(r'^clients/(?P<pk>\d+)/delete/$', views.ClientsDelete.as_view(), name='clients_delete'),
    re_path(r'^seasons/$', views.SeasonsListView.as_view(), name='seasons'),
    re_path(r'^seasons/(?P<pk>\d+)$', views.SeasonsDetailView.as_view(), name='seasons-detail'),
    re_path(r'^seasons/create/$', views.SeasonsCreate.as_view(), name='seasons_create'),
    re_path(r'^seasons/(?P<pk>\d+)/update/$', views.SeasonsUpdate.as_view(), name='seasons_update'),
    re_path(r'^seasons/(?P<pk>\d+)/delete/$', views.SeasonsDelete.as_view(), name='seasons_delete'),
    re_path(r'^tours/$', views.ToursListView.as_view(), name='tours'),
    re_path(r'^tours/(?P<pk>\d+)$', views.ToursDetailView.as_view(), name='tours-detail'),
    re_path(r'^tours/create/$', views.ToursCreate.as_view(), name='tours_create'),
    re_path(r'^tours/(?P<pk>\d+)/update/$', views.ToursUpdate.as_view(), name='tours_update'),
    re_path(r'^tours/(?P<pk>\d+)/delete/$', views.ToursDelete.as_view(), name='tours_delete'),
    re_path(r'^trips/$', views.TripsListView.as_view(), name='trips'),
    re_path(r'^trips/(?P<pk>\d+)$', views.TripsDetailView.as_view(), name='trips-detail'),
    re_path(r'^trips/create/$', views.TripsCreate.as_view(), name='trips_create'),
    re_path(r'^trips/(?P<pk>\d+)/update/$', views.TripsUpdate.as_view(), name='trips_update'),
    re_path(r'^trips/(?P<pk>\d+)/delete/$', views.TripsDelete.as_view(), name='trips_delete'),
]
