from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('list/', views.lists, name='lists'),
    path('list/<int:list_id>/', views.list_detail, name='detail'),
]

