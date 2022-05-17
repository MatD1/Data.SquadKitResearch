"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from myapi import views

admin.sites.AdminSite.site_header = 'SquadKitResearch Administration'
admin.sites.AdminSite.site_title = 'SquadKitResearch'
admin.sites.AdminSite.index_title = 'SquadKitResearch index'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate', views.genReport),
    path('', views.index),
    path('british-report', views.britishReport),
    path('insurgent-report', views.insurgentReport),
    path('australian-report', views.australianReport),
    path('canadian-report', views.canadianReport),
    path('report', views.allReport),
    path('api/', include('myapi.urls')),
]
