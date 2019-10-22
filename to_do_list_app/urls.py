from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('list/<int:list_id>/item/delete/<int:item_id>', views.item_delete, name='item_delete'),
    path('list/<int:list_id>/item/add/', views.item_add, name='item_add'),
    path('list/<int:list_id>/', views.list_detail, name='detail'),
    path('list/delete/<int:list_id>/', views.list_delete, name='delete_list'),
    path('list/add', views.list_add, name='list_add'),
    path('list/', views.lists, name='lists'),
    url(r'^$', views.index, name='index'),
]

