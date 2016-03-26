from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.WordView.as_view(), name='index'),
    url(r'^([\w-]+)/$', views.WordView.as_view(), name='index-char'),
]