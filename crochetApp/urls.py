from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shop/', views.shopIndex),
    path('logout/', views.logout),
    path('shop/logout/', views.shopLogout),
    path('login/', views.login),
    path('shop/login/', views.ownerLogin),
    path('signup/', views.signup),
    path('shop/signup/', views.ownerSignup),
    path('register/', views.register),
    path('shop/register/', views.ownerRegister),
    path('dashboard/', views.dashboard),
    path('shop/dashboard/', views.shopDashboard),
    path('shop/categories/', views.categories),
    path('shop/createCat/', views.createCat),
    path('shop/products/', views.products),
    path('shop/createProd/', views.createProduct),
]