from django.db import models

# Create your models here.
class Users(modesls.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.Charfield(max_length=50, verbose_name='First Name:', blank=False)
    last_name = models.Charfield(max_length=50, verbose_name='Last Name:', blank=False)
    username = models.Charfield(max_length=50, unique=True, blank=False)
    passwrod = models.Charfield(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    