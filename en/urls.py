from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.WordView.as_view(), name='index'),
]