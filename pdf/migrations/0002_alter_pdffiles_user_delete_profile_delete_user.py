# Generated by Django 4.2.10 on 2024-02-16 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pdf", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pdffiles",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
