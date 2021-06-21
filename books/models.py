from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)