"""
WebBasedTextSearcher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path
from django.conf.urls import include, url
import TextSearcher.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', TextSearcher.views.index, name='index'),
    url(r'^home$', TextSearcher.views.index, name='home'),
	url(r'^about$', TextSearcher.views.about, name='about'),
	url(r'^search-files$', TextSearcher.views.about, name='search_files'),
	url(r'^file-list/$', TextSearcher.views.file, name='file_list'),
]
