from django.shortcuts import render, redirect
from .models import Products, User, OwnerUser, Categories

FOOTER = {
    'Created by Melissa',
    'Thank you for visiting the Market Place'
}

# Main Landing page (general user sign-in)
def index(request):
    context = {
        'footer': FOOTER
    }
    return render(request, "index.html", context)

# Shop owner landing page
# def shopIndex(request):
#     context = {
#         'footer': FOOTER
#     }
#     return render(request, 'owner.html', context)

# General user register route
def register(request):
    if request.method == "GET":
        return redirect('/signup/')
    else:
        newUser = User.objects.register(request.POST)
        request.session['user_id'] = newUser.id
        return redirect('/dashboard/')

# Shop Owner Register route
# def ownerRegister(request):
#     if request.method == "GET":
#         return redirect('/shop-signup/')
#     else:
#         newOwnerUser = OwnerUser.objects.register(request.POST)
#         request.session['ownerUser_id'] = newOwnerUser.id
#         return redirect('/shop-dashboard/')

# General user login route
def login(request):
    if request.method == 'GET':
        return redirect('/')
    user = User.objects.get(username=request.POST['username'])
    request.session['user_id'] = user.id
    return redirect('/dashboard/')

# Shop owner login route
# def ownerLogin(request):
#     if request.method == 'GET':
#         return redirect('/owner')
#     ownerUser = OwnerUser.objects.get(ownerUsername=request.POST['ownerUsername'])
#     request.session['ownerUser_id'] = ownerUser.id
#     return redirect('/shop-dashboard/')

# Register landing page (for General Users)
def signup(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'register.html', context)

# Register landing page (for Shop Owners)
# def ownerSignup(request):
#     context = {
#         'footer': FOOTER
#     }
#     return render(request, 'ownerRegister.html', context)

def logout(request):
    # request.session.clear()
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'footer': FOOTER,
        'user': user,
        'allProducts': Products.objects.all().values()
    }
    return render(request, 'dashboard.html', context)

# def shopDashboard(request):
#     if 'ownerUser_id' not in request.session:
#         return redirect('/owner')
#     ownerUser = OwnerUser.objects.get(id=request.session['ownerUser_id'])
#     context = {
#         'footer': FOOTER,
#         'ownerUser': ownerUser,
#         'allProducts': Products.objects.all().values()
#     }
#     return render(request,'ownerDashboard.html', context)
