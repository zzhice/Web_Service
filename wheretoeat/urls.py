"""wheretoeat URL Configuration

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
from wheretoeat_app.views import *

from django.conf.urls import url


urlpatterns = [
    url(r'^$', start ,name='home'),
    url('^get_run/$', get_run, name='get_run'),
    url('^get_history/$', get_history, name='get_history'),
    url('^get_info/$', get_info, name='get_info'),
    url('^get_weather/$', get_weather, name='get_weather'),
]
