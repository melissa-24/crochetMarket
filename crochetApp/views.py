from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, OwnerUser, Category, Products

import bcrypt

# Used for all pages
FOOTER = {
    'Created by Melissa',
    'Thank you for visiting the Market Place'
}

# -----------------General User account pages and routes-----------------


# -------Main Landing page (general user sign-in)-------
def index(request):
    context = {
        'footer': FOOTER
    }
    return render(request, "index.html", context)

# -------General user login route-------
def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/')

# -------Register landing page (for General Users)-------
def signup(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'register.html', context)

# -------General user register route-------
def register(request):
    if request.method == 'GET':
        return redirect('/signup/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/signup/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        email = request.POST['email'],
        username = request.POST['username'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/dashboard/')

# -------General User Dashboard-------
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'footer': FOOTER,
        'user': user,
        'allProducts': Products.objects.all().values(),

    }
    return render(request, 'dashboard.html', context)

# -------General User Logout-------
def logout(request):
    request.session.clear()
    return redirect('/')

# User Single Product View
def singleProduct(request, product_id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    oneProd = Products.objects.get(id=product_id)
    context = {
        'footer': FOOTER,
        'user': user,
        'product': oneProd
    }
    return render(request, 'singleProduct.html', context)





# -----------------Shop Owner pages and routes-----------------


# -------Shop owner landing page-------
def shopIndex(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'owner.html', context)

# -------Shop owner login route-------
def ownerLogin(request):
    ownerUser = OwnerUser.objects.filter(ownerUsername = request.POST['ownerUsername'])
    if ownerUser:
        ownerUserLogin = ownerUser[0]
        if bcrypt.checkpw(request.POST['ownerPassword'].encode(), ownerUserLogin.ownerPassword.encode()):
            request.session['ownerUser_id'] = ownerUserLogin.id
            return redirect('/shop/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/shop/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/shop/')

# -------Register landing page (for Shop Owners)-------
def ownerSignup(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'ownerRegister.html', context)

# -------Shop Owner Register route-------
def ownerRegister(request):
    if request.method == 'GET':
        return redirect('/shop/signup/')
    errors = OwnerUser.objects.ownerValidate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/shop/')
    hashedOpw = bcrypt.hashpw(request.POST['ownerPassword'].encode(), bcrypt.gensalt()).decode()
    newOwnerUser = OwnerUser.objects.create(
        ownerFirstName = request.POST['ownerFirstName'],
        ownerLastName = request.POST['ownerLastName'],
        ownerUsername = request.POST['ownerUsername'],
        ownerEmail = request.POST['ownerEmail'],
        shopName = request.POST['shopName'],
        ownerPassword = hashedOpw
    )
    request.session['ownerUser_id'] = newOwnerUser.id
    return redirect('/shop/dashboard/')

# -------Shop Dashboard Landing Page-------
def shopDashboard(request):
    if 'ownerUser_id' not in request.session:
        return redirect('/shop')
    ownerUser = OwnerUser.objects.get(id=request.session['ownerUser_id'])
    context = {
        'footer': FOOTER,
        'ownerUser': ownerUser,
        'allProducts': Products.objects.all().values()
    }
    return render(request,'ownerDashboard.html', context)

# -------Shop Logout Route-------
def shopLogout(request):
    request.session.clear()
    return redirect('/shop/')

# -------Display Categories Landing Page-------
def categories(request):
    if 'ownerUser_id' not in request.session:
        return redirect('/shop')
    ownerUser = OwnerUser.objects.get(id=request.session['ownerUser_id'])
    context = {
        'footer': FOOTER,
        'ownerUser': ownerUser,
        'categories': Category.objects.all().values()
    }
    return render(request, 'categories.html', context)

# -------Create New Category Route-------
def createCat(request):
    Category.objects.create(
        catName=request.POST['catName']
    )
    return redirect('/shop/categories/')

# -------Edit Category Landing Page-------
def editCat(request, category_id):
    if 'ownerUser_id' not in request.session:
        return redirect('/shop')
    ownerUser = OwnerUser.objects.get(id=request.session['ownerUser_id'])
    oneCat = Category.objects.get(id=category_id)
    context = {
        'footer': FOOTER,
        'ownerUser': ownerUser,
        'cat': oneCat 
    }
    return render(request, 'editCategory.html', context)

# -------Update Category Route-------
def updateCat(request, category_id):
    toUpdate = Category.objects.get(id=category_id)
    toUpdate.catName = request.POST['catName']
    toUpdate.save()

    return redirect('/shop/categories/')

# -------Delete Category Route-------
def deleteCat(request, category_id):
    toDelete = Category.objects.get(id=category_id)
    toDelete.delete()

    return redirect('/shop/categories/')

# -------Display Products Landing Page-------
def products(request):
    if 'ownerUser_id' not in request.session:
        return redirect('/shop')
    ownerUser = OwnerUser.objects.get(id=request.session['ownerUser_id'])
    context = {
        'footer': FOOTER,
        'ownerUser': ownerUser,
        'products': Products.objects.all().values(),
        'shop': OwnerUser.objects.all().values()
    }
    return render(request, 'products.html', context)

# -------Create New Product Route-------
def createProduct(request):
    if 'ownerUser_id' not in request.session:
        return redirect('/shop')
    ownerUser = OwnerUser.objects.get(id=request.session['ownerUser_id'])
    ownerShop = OwnerUser.objects.get(id = request.POST['ownerUser_id'])

    newProducts = Products.objects.create(
        itemName = request.POST['itemName'],
        itemDescription = request.POST['itemDescription'],
        itemPrice = request.POST['itemPrice'],
        itemImg = request.POST['itemImg'],
        itemShop = ownerShop
    )
    return redirect('/shop/products/')
