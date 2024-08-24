from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('background/', views.background_view, name='background'),
    path('treatment/', views.treatment_view, name='treatment'),
    path('public-conduct/', views.public_conduct_view, name='public_conduct'),
    path('celiac-associations/', views.celiac_associations_view, name='celiac_associations'),
    path('entitlements/', views.entitlements_view, name='entitlements'),
    path('recipes/', views.recipes_view, name='recipes'),
    path('recipes/delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('like/', views.like_recipe, name='like_recipe'),  # type: ignore
    path('recipe/<int:pk>/', views.add_comment, name='add_comment'), # type: ignore
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),




    path('army/', views.army_view, name= 'army'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('preferences/', views.Preferences_view, name='preferences'), 
    path('comments/', views.comments_view, name='comments'),
    path('notifications/', views.notifications_view, name='notifications'),

  

       
]


