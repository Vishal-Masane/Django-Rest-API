# Generated by Django 5.0.2 on 2024-05-27 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookslibrary',
            name='Name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]