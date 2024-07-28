from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import backGround, TreatmentMethod, PublicConduct, CeliacAssociation, Entitlement, Recipe
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

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

def login_view(request):
    if request.method == 'post':
        pass 
    return render(request, 'login.html')

def login_page(request):
    return render(request, 'login.html')

def registration_page(request):
    return render(request, 'registration.html')


