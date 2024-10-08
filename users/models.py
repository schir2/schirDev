from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ...


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
