from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', default=False) #new field added
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class SecOne(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='secone/', default=False)

    def __str__(self):
        return self.name
    
class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField() 

    def __str__(self):
        return self.title