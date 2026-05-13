
from django.utils.http import content_disposition_header
from django.db import models

# Create your models here.
class Category(models.Model):
  name= models.CharField(max_length=100)
  ico= models.CharField(max_length=50, help_text="Icon CSS Class")

  def __clase__(self):
    return self.name 

class Manual(models.Model):
  title = models.CharField(max_length=200)
  slug = models.SlugField(unique=True)
  content=models.TextField()
  Category =models.ForeignKey(Category, on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
