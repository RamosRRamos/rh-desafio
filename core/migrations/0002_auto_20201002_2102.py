# Generated by Django 3.1.1 on 2020-10-02 21:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Foto do serviço'),
        ),
    ]
