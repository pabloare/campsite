from django.db import models
from manager.models import Dish, Seat


class Order(models.Model):
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE, related_name='seat')
    note = models.CharField(max_length=300)
    dishes = models.ManyToManyField(Dish)
