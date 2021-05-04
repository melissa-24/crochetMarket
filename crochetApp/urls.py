from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('signup/', views.signup),
    path('logout/', views.logout),
    path('dashboard/', views.dashboard),
]