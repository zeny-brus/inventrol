from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Category (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product (models.Model):
    name = models.CharField( verbose_name='product', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amout = models.PositiveIntegerField()
    min_amout = models.PositiveSmallIntegerField()
    
    TYPE_UNIT = [
        ('un','unidade'),
        ('kg','kilograma'),
        ('gr','grama'),
        ('dz','duzia'),
        ('m2','metro quadrado'),
        ('m3','metro cubico'),
        ('mt','metro'),
        ('lt','litro'),
    ]
    uni = models.CharField(max_length=20, choices=TYPE_UNIT)

    

    def __str__(self):
        return self.name

class Movement (models.Model):
    TYPE_MOVEMENT = [
        ('ENTRY','entry'),
        ('OUTPUT','output'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_movement = models.CharField(max_length=10, choices=TYPE_MOVEMENT)
    amout = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        data_format = self.date.strftime('%H:%M %d/%m/%Y')
        return f'{self.type_movement} - {self.product.name} - {data_format} '
    
    def save(self, *args, **kwargs):
        if not self.user.id:
            self.user = kwargs.pop('user',None)
        super().save(*args, **kwargs)
