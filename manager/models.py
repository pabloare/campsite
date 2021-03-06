from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save


class Restaurant(models.Model):
    name = models.CharField(max_length=80, null=True)
    autoserve = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=5000, null=True)

    def __str__(self):
        return self.name


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')
    email = models.EmailField(max_length=150, null=True)
    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='profile_pictures', blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='manager')

    def __str__(self):
        return self.user.username


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='table')
    table_number = models.IntegerField(default=0)

    def __str__(self):
        return str(self.table_number)


class Seat(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='seat')
    seat_number = models.IntegerField(default=0)
    payed = models.BooleanField(default=True)

    def __str__(self):
        return str(self.seat_number)


class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dish', default='')
    dish_number = models.IntegerField(default=0)
    name = models.CharField(null=True, max_length=100)
    description = models.CharField(max_length=500, default="")
    time_to_do = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
