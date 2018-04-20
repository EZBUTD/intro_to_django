from django.urls import path

from . import views

urlpatterns = [
path('',views.index1, name='index'),
path('sign/', views.sign1, name='sign'),
path('sign/<str:ID_value>/', views.sign_detail21, name='sign_detail21') #when the url contains any value after sign/, that value gets passed as ID_value
]

