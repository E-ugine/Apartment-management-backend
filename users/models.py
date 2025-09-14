from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        landlord = 'landlord', 'Landlord'
        caretaker = 'caretaker', 'Caretaker'
        tenant = 'tenant', 'Tenant'
        
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.tenant)

    def __str__(self):
        return f"{self.username} ({self.role})"
