from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, MinLengthValidator
from django.contrib.auth.password_validation import validate_password

# Create your models here.
class Users(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name='First Name:', blank=False, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, verbose_name='Last Name:', blank=False, validators=[MinLengthValidator(2)])
    username = models.CharField(max_length=50, unique=True, blank=False, validators=[MinLengthValidator(2)])
    password = models.CharField(blank=False, max_length=127)
    email = models.EmailField(unique=True, blank=False, validators=[EmailValidator()])
    grad_year = models.CharField(blank=False, max_length=4)
    

    