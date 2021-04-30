from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signup/', views.signup),
    path('logout/', views.logout),
    path('dashboard/', views.dashboard),
    path('add-new/', views.addNew)
]