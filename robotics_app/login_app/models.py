from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name='First Name:', blank=False)
    last_name = models.CharField(max_length=50, verbose_name='Last Name:', blank=False)
    username = models.CharField(max_length=50, unique=True, blank=False)
    password = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    