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
from weig import views, searchdir, formexam
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name = 'login.html')),
    url(r'^loginResult', views.login, name="login_commit"),

    url('^dir/$', TemplateView.as_view(template_name = 'searchdir.html')),
    url('^search/$', searchdir.search),
    url('^search_post/$', searchdir.search_post),

    url('^formExample/$', TemplateView.as_view(template_name = 'formExam.html')),
    url('^form/$', formexam.formExample),
    url('^form2/$', formexam.formExample2),

    url('^accessDB/$', dbaccess.browse),
    url('^addBook/$', dbaccess.addBook),
    url('^addBookOwner/$', dbaccess.addBookOwner),

    url(r'^admin/', admin.site.urls),
]
