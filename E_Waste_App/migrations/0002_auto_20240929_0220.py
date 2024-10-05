# Generated by Django 5.1.1 on 2024-09-28 23:20

from django.db import migrations
from django.contrib.auth.models import User

def create_default_admin(apps, schema_editor):
    User.objects.create_superuser(
        username='admin',
        email='admin@gmail.com',
        password='12345Admin..'  # Change this to a secure password
    )

class Migration(migrations.Migration):
    dependencies = [
        ('E_Waste_App', '0001_initial'),  # Replace with your last migration
    ]

    operations = [
        migrations.RunPython(create_default_admin),
    ]