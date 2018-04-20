from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_guest, name='index_guest'),
    path('sign_guest/', views.sign_guest, name='sign_guest')
]
