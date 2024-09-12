from importlib.metadata import requires
from os import name
import select
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import backGround, TreatmentMethod, PublicConduct, CeliacAssociation, celiac_army
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Preferences, Recipe, Like, CommentRecipe,Product
from .forms import ProfileForm, PreferencesForm, RecipeForm, Comment_RecipeForm, ProductForm
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
@login_required
def home_view(request): # type: ignore
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


def is_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})        


@login_required
@user_passes_test(is_admin)
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})        

@login_required
@user_passes_test(is_admin)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def recipes_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('recipes')  # Redirect to recipes list after saving
    else:
        form = RecipeForm()  # Create an empty form for GET requests
    recipes = Recipe.objects.all().order_by('-created_at')  # Order by creation date/time (optional)
    return render(request, 'recipes.html', {'recipes': recipes, 'form': form})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipes = form.save(commit=False)
            recipes.user = request.user
            recipes.save()
            return redirect('recipes')
        else:
            print(form.errors)  
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})



def recipe_list(request):
    recipe_list = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipe_list': recipe_list})



def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')
    return render(request, 'confirm_delete.html', {'recipe': recipe})

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes')
        
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})    



    

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

@login_required
def profile_view(request):
    # מנסה למצוא את פרופיל המשתמש הנוכחי
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # אם פרופיל לא נמצא, צור פרופיל חדש
        profile = Profile.objects.create(user=request.user, bio='', profile_picture=None)
    
    # טיפול בבקשת POST כדי לעדכן פרופיל
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # הפנה מחדש לדף פרופיל אחרי שמירת השינויים
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'profile.html', {'profile': profile, 'form': form})

@login_required
def update_preferences(request):
    preferences, created = Preferences.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PreferencesForm(request.POST, instance=preferences)
        if form.is_valid():
            form.save()
            return redirect('view_preferences')  # Redirect to a page showing updated preferences or a success message
    else:
        form = PreferencesForm(instance=preferences)

    recipes = Recipe.objects.all()
    products = Product.objects.all()

    return render(request, 'preferences.html', {
        'form': form,
        'recipes': recipes,
        'products': products,
    })

@login_required
def view_preferences(request):
    preferences = Preferences.objects.get(user=request.user)
    return render(request, 'view_preferences.html', {
        'preferences': preferences,
    })



            

def like_recipe(request):
    user = request.user
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        recipe_obj = Recipe.objects.get(id=recipe_id)

        if user in recipe_obj.likes.all():
            recipe_obj.likes.remove(user)
        else:
            recipe_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, recipe_id=recipe_id)    

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()            

        return redirect('recipes')
     


@login_required
def add_comment(request, pk):
    recipe = Recipe.objects.get(id=pk)

    form = Comment_RecipeForm(instance=recipe)

    if request.method == 'POST':
        form = Comment_RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            name = request.user.username
            body2 = form.cleaned_data['body']
            comment = CommentRecipe(
                parent_recipe=recipe,
                body=body2,
                user=request.user,
                created_at=datetime.now())
            comment.save()
            return redirect('recipes')
        else:
            print('form is invalid')

    else:
        form = Comment_RecipeForm()    


    context = {
        'form': form
    }
  

    return render(request, 'add_comment.html', context)                
                

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(CommentRecipe, id=comment_id, user=request.user)
    if request.method == 'POST':
        form = Comment_RecipeForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('recipes')
    else:
        form = Comment_RecipeForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})



  
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(CommentRecipe, id=comment_id, user=request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('recipes')
    return render(request, 'delete_comment.html', {'comment': comment})   



def search_results(request):
    query = request.GET.get('q').strip()
    recipes = Recipe.objects.filter(name__icontains=query)
    products = Product.objects.filter(name__icontains=query)
    print(f"Query: {query}")
    print(f"Recipes: {recipes}")

    

    context = {
        'query': query,
        'recipes': recipes,
        'products': products
    }
    return render(request, 'search_results.html', context)