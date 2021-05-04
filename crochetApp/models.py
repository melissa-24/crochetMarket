from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Products

class Products(models.Model):
    itemName = models.CharField(max_length=45)
    itemDescription = models.TextField()
    itemPrice = models.CharField(max_length=45)
    itemImg = models.CharField(max_length=255)

# General users

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['firstName']) < 2:
            errors['firstName'] = 'First Name must be at least 2 characters'

        if len(form['lastName']) < 2:
            errors['lastName'] = 'Last Name must be at least 2 characters'

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

    def authenticate(self, username, password):
        users = self.filter(username=username)
        if not users:
            return False
        
        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            firstName = form['firstName'],
            lastName = form['lastName'],
            email = form['email'],
            username = form['username'],
            password = pw
        )

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    objects = UserManager()

# Shop owners

class OwnerUserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['ownerFirstName']) < 2:
            errors['ownerFirstName'] = 'First Name must be at least 2 characters'

        if len(form['ownerLastName']) < 2:
            errors['ownerLastName'] = 'Last Name must be at least 2 characters'

        if not EMAIL_REGEX.match(form['ownerEmail']):
            errors['ownerEmail'] = 'Invalid Email Address'

        ownerEmailCheck = self.filter(email=form['ownerEmail'])
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

    def authenticate(self, ownerUsername, ownerPassword):
        ownerUsers = self.filter(ownerUsername=ownerUsername)
        if not ownerUsers:
            return False
        
        ownerUser = OwnerUsers[0]
        return bcrypt.checkpw(ownerPassword.encode(), ownerUser.ownerPassword.encode())

    def register(self, form):
        opw = bcrypt.hashpw(form['ownerPassword'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            ownerFirstName = form['ownerFirstName'],
            ownerLastName = form['ownerLastName'],
            ownerEmail = form['ownerEmail'],
            ownerUsername = form['ownerUsername'],
            shopName = form['shopName'],
            ownerPassword = opw
        )

class OwnerUser(models.Model):
    ownerFirstName = models.CharField(max_length=45)
    ownerLastName = models.CharField(max_length=45)
    ownerEmail = models.EmailField(unique=True)
    ownerUsername = models.CharField(max_length=45)
    shopName = models.CharField(max_length=50)
    ownerPassword = models.CharField(max_length=45)

    objects = OwnerUserManager()