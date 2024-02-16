from django.db import models
from django.contrib.auth.models import User


class PdfFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=200)
    file_url = models.URLField(max_length=200)
