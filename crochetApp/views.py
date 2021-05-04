from django.shortcuts import render, redirect
from .models import Products, User, OwnerUser

FOOTER = {
    'Created by Melissa',
    'Thank you for visiting the Django Market'
}

def index(request):
    context = {
        'footer': FOOTER
    }
    return render(request, "index.html", context)

def register(request):
    if request.method == "GET":
        return redirect('/signup/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/signup/')
    else:
        newUser = User.objects.register(request.POST)
        request.session['user_id'] = newUser.id
        return redirect('/dashboard/')

def ownerRegister(request):
    if request.method == "GET":
        return redirect('/ownerSignup/')
    errors = OwnerUser.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/ownerSignup/')
    else:
        newOwnerUser = OwnerUser.objects.register(request.POST)
        request.session['ownerUser_id'] = newOwnerUser.id
        return redirect('/OwnerDashboard/')

def login(request):
    if request.method == 'GET':
        return redirect('/')
    if not User.objects.authenticate(request.POST['username'], request.POST['password']):
        messages.error(request, 'Invalid Username/Password')
        return redirect('/')
    user = User.objects.get(username=request.POST['username'])
    request.session['user_id'] = user.id
    return redirect('/dashboard/')

def signup(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'register.html', context)

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
