from django.contrib import admin
from .models import Products, User, OwnerUser

admin.site.register(Products)
admin.site.register(User)
admin.site.register(OwnerUser)
