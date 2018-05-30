from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Restaurant(models.Model):
    name = models.CharField(max_length=80, null=True)


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')
    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='profile_pictures', blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='manager')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Manager.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='table')
    table_number = models.IntegerField(primary_key=True)


class Seat(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='seat')
    seat_number = models.IntegerField(primary_key=True)


class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dish')
    dish_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
