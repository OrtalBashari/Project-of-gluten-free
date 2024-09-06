from django.contrib import admin
from .models import backGround, TreatmentMethod, Recipe, Like, CommentRecipe, Product

# Register your models here.

admin.site.register(backGround)
admin.site.register(TreatmentMethod)
admin.site.register(Recipe)
admin.site.register(Like)
admin.site.register(CommentRecipe)


@admin.register(Product)
class GlutenFreeProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'link')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    ordering = ('name',)

