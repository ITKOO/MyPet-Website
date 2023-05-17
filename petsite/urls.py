from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('introduce', views.introduce, name='introduce'),
    path('message', views.message_list, name='message_list'),
    path('gallery', views.gallery, name='gallery'),
    path('snack_list', views.snack_list, name='snack_list'),
]
