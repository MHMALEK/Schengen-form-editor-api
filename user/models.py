from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics/")
    phone_number = models.CharField(max_length=15)
    email = models.EmailField((""), max_length=254)
