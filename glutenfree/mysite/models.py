from django.db import models

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
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name



