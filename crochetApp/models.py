from django.db import models
import re
# import bcrypt

# General users

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['firstName']) < 2:
            errors['firstName'] = 'First Name must be at least 2 characters'

        if len(form['lastName']) < 2:
            errors['lastName'] = 'Last Name must be at least 2 characters'

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'

        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email Address already in use'

        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already in use'

        if len(form['password']) < 6:
            errors['password'] = 'Password must be at least 6 characters'

        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'

        return errors

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    objects = UserManager()

    userCreatedAt = models.DateTimeField(auto_now_add=True)
    userUpdatedAt = models.DateTimeField(auto_now=True)

# Shop owners

class OwnerUserManager(models.Manager):
    def ownerValidate(self, form):
        errors = {}
        if len(form['ownerFirstName']) < 2:
            errors['ownerFirstName'] = 'First Name must be at least 2 characters'

        if len(form['ownerLastName']) < 2:
            errors['ownerLastName'] = 'Last Name must be at least 2 characters'

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(form['ownerEmail']):
            errors['ownerEmail'] = 'Invalid Email Address'

        ownerEmailCheck = self.filter(ownerEmail=form['ownerEmail'])
        if ownerEmailCheck:
            errors['ownerEmail'] = 'Email Address already in use'

        ownerUsernameCheck = self.filter(ownerUsername=form['ownerUsername'])
        if ownerUsernameCheck:
            errors['ownerUsername'] = 'Username already in use'

        shopNameCheck = self.filter(shopName=form['shopName'])
        if shopNameCheck:
            errors['shopName'] = 'Shop Name already in use'

        if len(form['ownerPassword']) < 6:
            errors['ownerPassword'] = 'Password must be at least 6 characters'

        if form['ownerPassword'] != form['confirm']:
            errors['ownerPassword'] = 'Passwords do not match'

        return errors

class OwnerUser(models.Model):
    ownerFirstName = models.CharField(max_length=45)
    ownerLastName = models.CharField(max_length=45)
    ownerEmail = models.EmailField(unique=True)
    ownerUsername = models.CharField(max_length=45)
    shopName = models.CharField(max_length=50)
    ownerPassword = models.CharField(max_length=45)

    objects = OwnerUserManager()

    ownerUserCreatedAt = models.DateTimeField(auto_now_add=True)
    ownerUserUpdatedAt = models.DateTimeField(auto_now=True)

# Products

class Products(models.Model):
    itemName = models.CharField(max_length=45)
    itemDescription = models.TextField()
    itemPrice = models.CharField(max_length=45)
    itemImg = models.CharField(max_length=255)
    itemShop = models.ForeignKey(OwnerUser, related_name='shop', on_delete=models.CASCADE)

# Categories
class Category(models.Model):
    catName = models.CharField(max_length=45)
    assignedCat = models.ManyToManyField(Products, related_name='categories')