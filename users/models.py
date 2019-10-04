from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  email = models.EmailField(max_length=200)
  first_name = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)

  def __str__(self):
    return self.email