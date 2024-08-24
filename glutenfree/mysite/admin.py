from django.contrib import admin
from .models import backGround, TreatmentMethod, Recipe, Like, CommentRecipe

# Register your models here.

admin.site.register(backGround)
admin.site.register(TreatmentMethod)
admin.site.register(Recipe)
admin.site.register(Like)
admin.site.register(CommentRecipe)

