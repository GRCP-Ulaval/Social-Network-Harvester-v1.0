"""SocialNetworkHarvester_v1p0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from .views.charts import *
from .views.downloads import *
from .views.ajaxTables import *

urlpatterns = [
    url(r'linechart/?$', lineChart),
    url(r'piechart/?$', pieChart),
    url(r'geographic/?$', geoChart),
    url(r'bubblechart/?$', bubbleChart),
    url(r'distributionchart/?$', distributionChart),
    url(r'download/?$', downloadMedia),
    url(r'table/downloadProgress/?$', downloadProgress),
    url(r'table/ajax/?$', ajaxBase),
    url(r'table/selection/?$', setUserSelection),
]
