"""djangoweb URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from testmodel import dbaccess
from weig import views, searchdir

urlpatterns = [
    url('^$', views.main),
    url('^dir/$', searchdir.index),

    url('^search/$', searchdir.search),
    url('^search_post/$', searchdir.search_post),
    url('^form/$', searchdir.formExample),

    url('^dbadd/$', dbaccess.add),
    url('^accessDB/$', dbaccess.browse),

    url(r'^admin/', admin.site.urls),
]
