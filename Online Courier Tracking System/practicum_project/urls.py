"""practicum_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from centeradmin import views

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^search/', include('haystack.urls')),
    url(r'^sms/', views.sms, name='sms'),
    url(r'^online/', views.online, name='online'),
    url(r'^submit/', views.submit, name='submit'),
    url(r'^cancel/', views.cancel, name='cancel'),
    url(r'^cancelled/', views.cancelled, name='cancelled'),
    url(r'^submitfeedback/', views.submitfeedback, name='feedback')

]
