from django.contrib import admin
from .models import User, OwnerUser, Category, Products

admin.site.register(User)
admin.site.register(OwnerUser)
admin.site.register(Category)
admin.site.register(Products)