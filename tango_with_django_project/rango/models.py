from django.db import models

# Create your models here.
# models.Model is the base class for all models in Django.
class Category(models.Model):
    # max_length is the max length of the field in the database, unique=True ensures that no two categories can have the same name
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name
    
class Page(models.Model):
    # ForeignKey is used to create a many-to-one relationship between Page and Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)  # Automatically set the field to now every time the object is saved
    def __str__(self):
        return self.title
"""
python manage.py migrate在初次执行的时候会创建django所有的表，包括auth_user表等。这些表django框架自带的applications会自动创建。
"""
