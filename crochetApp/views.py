from django.shortcuts import render, redirect
from .models import Products

FOOTER = {
    'Created by Melissa',
    'Thank you for visiting the Django Market'
}

def index(request):
    context = {
        'footer': FOOTER
    }
    return render(request, "index.html", context)

def signup(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'register.html', context)

def logout(request):
    # request.session.clear()
    return redirect('/')

def dashboard(request):
    context = {
        'footer': FOOTER,
        'username': 'Melissa',
        'allProducts': Products.objects.all().values()
    }
    return render(request, 'dashboard.html', context)