from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('owner/', views.shopIndex),
    path('login/', views.login),
    # path('shop-login/', views.ownerLogin),
    path('signup/', views.signup),
    # path('shop-signup/', views.ownerSignup),
    path('register/', views.register),
    # path('shop-register/', views.ownerRegister),
    path('logout/', views.logout),
    path('dashboard/', views.dashboard),
    # path('shop-dashboard/', views.shopDashboard),
    path('categories/', views.categories),
    path('createCat/', views.createCat),
]