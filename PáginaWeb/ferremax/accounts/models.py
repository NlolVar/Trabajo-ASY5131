

from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('cliente','Cliente'),
        ('admin','Admin'),
        ('vendedor','Vendedor'),
        ('bodeguero','Bodeguero'),
        ('contador','Contador'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default='cliente')# Create your models here.
