from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=100, help_text="ProductName")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100,help_text="Description")

    def __str__(self):
        return self.name

class User(models.Model):

    name = models.CharField(max_length=100, help_text="UserName")
    password = models.CharField(max_length=100, help_text="UserPassword")
    shopping_cart = models.ManyToManyField(Product)


    def __str__(self):
        return self.name
