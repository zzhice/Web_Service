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
from django.contrib import admin
from django.urls import path
from wheretoeat_app.views import *
from django.conf.urls import url, include

from django.conf.urls import url

# call_api = [
#     url(r'^history$', show_history, name='history'),
#     url(r'^recommendation$', show_recommendation, name='recommendation'),
#     url(r'^res_list$', show_res_list, name='res_list'),
#     url(r'^est_time$', show_est_time, name='est_time'),
#     url(r'^directions$', show_directions, name='directions'),
# ]


urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', index,name='home'),
    url('^get_json/$', get_json, name='get_json'),
    # url('^api/$', include(call_api)),
]
