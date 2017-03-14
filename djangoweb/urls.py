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
from django.conf.urls import include, url
from django.contrib import admin
from django.views import static
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from chapter1 import placeholder
from testmodel import dbaccess
from testmodel.views import TestModelView
from weig import views, searchdir, formexam, ajaxexam
from chapter2 import views_ch2
from . import settings
from board.urls import router

urlpatterns = [

    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_URL}),
    # 如果没有建static文件夹，而是直接在根目录下建立的JS,CSS和Images文件夹，就将下面的三行代码注释去掉，删除上方的代码
    url( r'^js/(?P<path>.*)$', static.serve,{ 'document_root': settings.STATIC_URL }),
    url( r'^css/(?P<path>.*)$', static.serve, { 'document_root': settings.STATIC_URL }),
    url( r'^images/(?P<path>.*)$', static.serve, { 'document_root': settings.STATIC_URL }),

    url(r'^$',TemplateView.as_view(template_name = 'login.html')),
    url(r'^loginResult', views.login, name="login_commit"),

    url('^dir/$', TemplateView.as_view(template_name = 'searchdir.html')),
    url('^search/$', searchdir.search),
    url('^search_post/$', searchdir.search_post),

    url('^ajaxExam/$', TemplateView.as_view(template_name = 'ajaxExam.html'), name='ajaxExam'),
    url('^test_ajax/$', ajaxexam.test_ajax, name='test_ajax'),
    url('^test_ajaxPost/$', ajaxexam.test_ajax_post, name='test_ajax_post'),

    url('^formExample/$', TemplateView.as_view(template_name = 'formExam.html')),
    url('^form/$', formexam.formExample),
    url('^form2/$', formexam.formExample2),

    url('^accessDB/$', dbaccess.browse),
    url('^addBook/$', dbaccess.addBook),
    url('^addBookOwner/$', dbaccess.addBookOwner),

    url('^accessDB_oo/$', TestModelView.as_view()),
    url('^accessDB_oo/([\w-]+)/$', TestModelView.as_view(), name="accessDB_book_oo"),
    url('^accessDB_oo/(?P<id>[0-9]+)/$', TestModelView.as_view(), name="accessDB_BookOfOwner_oo"),
    url('^addBook_oo/$', TestModelView.as_view()),
    url('^addBookOwner_oo/$', TestModelView.as_view()),

    url('^chapter1/$', placeholder.entry),
     url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder.placeholder, name='placeholder'),

    url(r'^chapter2/(?P<slug>[\w./-]+)/$', views_ch2.page, name='page'),
    url(r'^chapter2/$', views_ch2.page, name='homepage'),

    #url(r'^admin/', admin.site.urls),

    url(r'^scrum/token/', obtain_auth_token, name='api-token'),
    url(r'^scrum/', include(router.urls)),

    url(r'^ss/$',TemplateView.as_view(template_name = 'board/index.html')),
]
