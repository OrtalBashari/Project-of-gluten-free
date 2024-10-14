from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('background/', views.background_view, name='background'),
    path('treatment/', views.treatment_view, name='treatment'),
    path('public-conduct/', views.public_conduct_view, name='public_conduct'),
    path('celiac-associations/', views.celiac_associations_view, name='celiac_associations'),
    path('army/', views.army_view, name= 'army'),

    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),




    path('recipes/', views.recipes_view, name='recipes'),
    path('recipes/delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('like/', views.like_recipe, name='like_recipe'), # type: ignore
    path('recipe/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),







    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('preferences/', views.update_preferences, name='update_preferences'),
    path('preferences/view/', views.view_preferences, name='view_preferences'), 
    path('search/', views.search_results, name='search_results'),
    path('about/', views.about, name='about'),



  

       
]


