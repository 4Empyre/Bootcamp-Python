from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.temp),
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^[0-9]{6}/$', views.show),
    url(r'^[0-9]{6}/edit/$', views.edit),
    url(r'^[0-9]{6}/delete/$', views.destroy),
]
