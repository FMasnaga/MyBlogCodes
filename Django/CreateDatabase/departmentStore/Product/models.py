from django.db import models

# Create your models here.
class Product (models.Model):
    name = models.CharField (max_length = 60)
    description = models.TextField (blank = True)
    remainingQuantity = models.PositiveIntegerField()
    price = models.DecimalField (max_digits= 6, decimal_places= 2)
    active = models.BooleanField (default= True)
    

    def __str__(self):
        return self.name