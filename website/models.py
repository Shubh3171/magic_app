from django.db import models
from django import forms

# Create your models here.


class Styling(models.Model):
    company = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    purp = models.TextField(max_length=200)
    file = models.FileField(upload_to="Styling/", null=True, default=None)

class Design(models.Model):
    company = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    purp = models.TextField(max_length=200)
    file = models.FileField(upload_to="Design/", null=True, default=None)

class Prototype(models.Model):
    company = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    purp = models.TextField(max_length=200)
    file = models.FileField(upload_to="Prototype/", null=True, default=None)

class CAE(models.Model):
    company = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    purp = models.TextField(max_length=200)
    file = models.FileField(upload_to="CAE/", null=True, default=None)

    

