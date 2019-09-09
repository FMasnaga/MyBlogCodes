from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):
    user = models.OneToOneField (User, on_delete = models.CASCADE)
    aboutMe = models.TextField ()
    country = models.CharField (max_length= 60)