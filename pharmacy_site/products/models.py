from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Product(models.Model):

    name = models.CharField(max_length=100, help_text="ProductName")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100,help_text="Description")

    def __str__(self):
        return self.name

class MyUser(models.Model):
    name = models.CharField(max_length=100, help_text="UserName")
    password = models.CharField(max_length=100, help_text="password")
    surname = models.CharField(max_length=100, help_text="UserSurname")
    telephone_number = models.CharField(max_length=100, help_text="UserTelephone")
    email = models.CharField(max_length=100, help_text="UserEmail")
    perms = models.IntegerField(default=0)
    token = models.CharField(max_length=100, help_text="token")

    def __str__(self):
        return self.name
