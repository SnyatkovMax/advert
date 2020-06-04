from django.db import models


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


class Country(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)
    description = models.CharField(max_length=500, unique=False, null=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    beds = models.PositiveIntegerField(null=True, default=0)
    baths = models.PositiveIntegerField(null=True, default=0)
    floors = models.PositiveIntegerField(null=True, default=1)
    metro = models.CharField(max_length=50, unique=False, null=True)
    area = models.FloatField(null=True, default=0)
    size = models.FloatField(null=True, default=0)
    photoURL = models.URLField(null=True)
    videoURL = models.URLField(null=True)
    photo = models.FileField(null=False, upload_to='upload/')
    address = models.CharField(max_length=100, unique=False, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} / {self.type} / {self.status} / {self.location} / {self.beds} / {self.baths} / ' \
               f'{self.floors} / {self.metro} / {self.area} / {self.size} / {self.address} / {self.city} / ' \
               f'{self.country}'
