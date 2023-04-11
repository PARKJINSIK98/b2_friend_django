from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10)
    region = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
