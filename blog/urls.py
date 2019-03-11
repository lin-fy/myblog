from django.urls import re_path
from . import views

app_name = 'blog'

urlpatterns = [
    re_path(r'^index/$', views.index),
    re_path(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    re_path(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    re_path(r'^edit/action$', views.edit_action, name='edit_action'),
]