from django.db import models

# Create your models here.

class products(models.Model):
    name=models.CharField(unique=True,max_length=100)
    price=models.PositiveBigIntegerField()
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=50)
    image=models.ImageField(null=True)
    
    
    def __str__(self):
        return self.name
    
    
    
    