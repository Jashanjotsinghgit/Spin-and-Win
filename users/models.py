from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    is_verified = models.BooleanField(default=False)
    has_spun = models.BooleanField(default=False)

    # Fix the error by specifying related_name attributes
    groups = models.ManyToManyField(Group, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions")
