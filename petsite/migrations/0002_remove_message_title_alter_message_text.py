# Generated by Django 4.2.1 on 2023-05-17 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='title',
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(max_length=30),
        ),
    ]
