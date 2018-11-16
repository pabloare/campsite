from django.db import models
from django.contrib.auth.models import User


class Cafe(models.Model):
    name = models.CharField(max_length=80, null=True)
    stripe_id = models.CharField(max_length=5000, null=True)

    def __str__(self):
        return self.name


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    email = models.EmailField(max_length=150, null=True)
    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='profile_pictures', blank=True)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='owner')
    is_owner = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Menu(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='menu', default='')
    name = models.CharField(max_length=500, default="")
    description = models.TextField(default="")


class Terminal(models.Model):
    name = models.CharField(max_length=500, default="")
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='terminal', default='')
    active = models.BooleanField(default=False)


class Item(models.Model):
    menu = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='item', default='')
    name = models.CharField(null=True, max_length=100)
    description = models.CharField(max_length=500, default="")
    time_to_do = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
