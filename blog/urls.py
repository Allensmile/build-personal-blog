# coding: utf-8

from django.conf.urls import url

from . import views


app_name = 'blog'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'), # 将 index 视图函数改写为类视图
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'), # 将 detail 视图函数改写为类视图
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'), # 将 archives 视图函数改写为类视图
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'), # 将 category 视图函数改写为类视图
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'), # 添加 tag 视图函数
    # url(r'^search/$', views.search, name='search'),
]
