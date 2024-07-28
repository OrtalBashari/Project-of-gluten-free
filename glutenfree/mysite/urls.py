from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('background/', views.background_view, name='background'),
    path('treatment/', views.treatment_view, name='treatment'),
    path('public-conduct/', views.public_conduct_view, name='public_conduct'),
    path('celiac-associations/', views.celiac_associations_view, name='celiac_associations'),
    path('entitlements/', views.entitlements_view, name='entitlements'),
    path('recipes/', views.recipes_view, name='recipes'),
    path('login/', views.login_view, name='login'),
    path('login/', views.login_page, name='login'),
    path('register/', views.registration_page, name='register'),
    
]


