import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class backGround(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class TreatmentMethod(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self) :
        return self.title    

class PublicConduct(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class CeliacAssociation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Entitlement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def total_likes(self):
        return self.likes.all().count()

    def __str__(self):
        return self.name


class celiac_army(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True) 

    def __str__(self):
        return self.user.username

class Preferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.TextField(blank=True)
    favorite_recipes = models.ManyToManyField('Recipe', blank=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.content[:20]}' # type: ignore
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_likes')
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user.username} likes {self.recipe.name}"

    
class CommentRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        try:
            return f'{self.user.username}: {self.body[:30]}'
        except:
            return f' no user: {self.body[:30]}'






   