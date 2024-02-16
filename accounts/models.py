from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    martial_status = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    visa_type = models.CharField(max_length=15)