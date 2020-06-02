from django.db import models

from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)
    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)
    beds = models.PositiveIntegerField(null=True, default=0)
    baths = models.PositiveIntegerField(null=True, default=0)
    photo = models.FileField(null=False, upload_to='upload/')
    description = models.CharField(max_length=500, unique=False, null=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
