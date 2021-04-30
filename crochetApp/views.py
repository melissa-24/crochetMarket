from django.shortcuts import render, redirect

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
    }
    return render(request, 'dashboard.html', context)

def addNew(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'addItems.html', context)

def postNew(request):
    if request.method == 'GET':
        return redirect('/add-new')
    request.session['resultNew'] = {
        'itemTitle': request.POST['itemTitle'],
        'itemDescription': request.POST['itemDescription'],
        'itemPrice': request.POST['itemPrice'],
    }
    return redirect('/dashboard')