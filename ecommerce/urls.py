__author__ = 'hutomo'

from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
import views

urlpatterns = [
    url(r'^$', views.index ),
    url(r'^detail/([0-9])$', views.detail),
]