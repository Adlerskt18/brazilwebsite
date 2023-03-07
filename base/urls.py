from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.resultPage, name='result'),
    path('about/', views.aboutPage, name='about'),
]