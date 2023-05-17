from django.db import models
from django.utils import timezone


class Message(models.Model):
    text = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


class Gallery(models.Model):
    img_url = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.img_url


class Snack(models.Model):
    title = models.TextField()
    img_url = models.TextField()
    price = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
