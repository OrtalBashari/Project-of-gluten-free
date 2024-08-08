from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import backGround, TreatmentMethod, PublicConduct, CeliacAssociation, Entitlement, Recipe, celiac_army
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_view(request):
    return render(request, 'home.html')

def home_view(request):
    return render(request, 'home.html')

def background_view(request):
    backgrounds = backGround.objects.all()
    return render(request, 'background.html', {'backgrounds': backgrounds})

def treatment_view(request):
    treatments = TreatmentMethod.objects.all()
    return render(request, 'treatment.html', {'treatments': treatments})

def public_conduct_view(request):
    conducts = PublicConduct.objects.all()
    return render(request, 'public_conduct.html', {'conducts': conducts})

def celiac_associations_view(request):
    associations = CeliacAssociation.objects.all()
    return render(request, 'celiac_associations.html', {'associations': associations})

def entitlements_view(request):
    entitlements = Entitlement.objects.all()
    return render(request, 'entitlements.html', {'entitlements': entitlements})

def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})


def army_view(request):
    army = celiac_army.objects.filter(title__icontains='צה"ל')
    return render(request, 'Celiac_army.html', {'army': army})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Debug statement to check form data
        print("Form submitted:", username, email)

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return render(request, 'register.html')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('home')  # Replace 'login' with your actual login view name

    return render(request, 'register.html')


def password_reset_view(request):
    # Implement password reset logic here
    return render(request, 'password_reset.html')



