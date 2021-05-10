from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Products, User, OwnerUser, Category

# Used for all pages
FOOTER = {
    'Created by Melissa',
    'Thank you for visiting the Market Place'
}

# General User account pages and routes


# Main Landing page (general user sign-in)
def index(request):
    context = {
        'footer': FOOTER
    }
    return render(request, "index.html", context)

# General user login route
def login(request):
    if request.method == 'POST':
        attemptedLogin=User.objects.filter(username=request.POST['username'])
        if attemptedLogin:
            userLogin=attemptedLogin[0]
            if userLogin.password == request.POST['password']:
                request.session['user_id']=userLogin.id
                return redirect('/dashboard')
    messages.error(request, "That username does not exist please sign up")
    return redirect('/')

# Register landing page (for General Users)
def signup(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'register.html', context)

# General user register route
def register(request):
    if request.method == "GET":
        return redirect('/signup/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
            return redirect('/')
    else:
        newUser = User.objects.register(request.POST)
        request.session['user_id'] = newUser.id
        return redirect('/dashboard/')

# General User Dashboard
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

# General User Logout
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





# Shop Owner pages and routes


# Shop owner landing page
def shopIndex(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'owner.html', context)

# Shop owner login route
def ownerLogin(request):
    if request.method == 'POST':
        ownerAttemptedLogin=OwnerUser.objects.filter(ownerUsername=request.POST['ownerUsername'])
        if ownerAttemptedLogin:
            ownerUserLogin=ownerAttemptedLogin[0]
            if ownerUserLogin.ownerPassword == request.POST['ownerPassword']:
                request.session['ownerUser_id']=ownerUserLogin.id
                return redirect('/shop/dashboard')
    messages.error(request, "That username does not exist please sign up")
    return redirect('/shop/')

# Register landing page (for Shop Owners)
def ownerSignup(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'ownerRegister.html', context)

# Shop Owner Register route
def ownerRegister(request):
    if request.method == "GET":
        return redirect('/shop/signup/')
    errors = OwnerUser.objects.ownerValidate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
            return redirect('/')
    else:
        newOwnerUser = OwnerUser.objects.ownerRegister(request.POST)
        request.session['ownerUser_id'] = newOwnerUser.id
        return redirect('/shop/dashboard/')

# Shop Dashboard
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

# Shop Logout
def shopLogout(request):
    request.session.clear()
    return redirect('/shop/')

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

def createCat(request):
    Category.objects.create(
        catName=request.POST['catName']
    )
    return redirect('/shop/categories/')

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

def updateCat(request, category_id):
    toUpdate = Category.objects.get(id=category_id)
    toUpdate.catName = request.POST['catName']
    toUpdate.save()

    return redirect('/shop/categories/')

def deleteCat(request, category_id):
    toDelete = Category.objects.get(id=category_id)
    toDelete.delete()

    return redirect('/shop/categories/')

def products(request):
    if 'ownerUser_id' not in request.session:
        return redirect('/shop')
    ownerUser = OwnerUser.objects.get(id=request.session['ownerUser_id'])
    context = {
        'footer': FOOTER,
        'ownerUser': ownerUser,
        'products': Products.objects.all().values()
    }
    return render(request, 'products.html', context)

def createProduct(request):
    Products.objects.create(
        itemName = request.POST['itemName'],
        itemDescription = request.POST['itemDescription'],
        itemPrice = request.POST['itemPrice'],
        itemImg = request.POST['itemImg'],
        category_id = request.POST['itemCat'],
        ownerUser_id = request.POST['itemShop']
    )
    return redirect('/shop/products/')
