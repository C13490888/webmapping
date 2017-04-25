"""webmapping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.gis import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView
from webm_app import views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', favicon_view),
    url(r'^machines/$', views.PndMachineView.as_view(), name='pndmachine-list'),
    url(r'^outlets/$', views.PndOutletView.as_view(), name='pndoutlet-list'),
    url(r'^machines/(?P<pk>[\d]+)/$', views.PndMachineIdView.as_view(), name='pndmachine-instance'),
    url(r'^outlets/(?P<pk>[\d]+)/$', views.PndOutletIdView.as_view(), name='pndoutlet-instance'),
    url(r'^machines/location/(?P<location>[\w])/$', views.PndMachineLocationView.as_view(), name='pndmachine-list-location'),
    #url(r'^outlets/location/(?P<location>[\w])/$', views.PndOutletLocationView.as_view(), name='pndoutlet-list-location'),

]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += staticfiles_urlpatterns()