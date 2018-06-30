from django.db import models
from manager.models import Dish, Seat


class Order(models.Model):
    username = models.CharField(max_length=30, default="noUsername")
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE, related_name='seat')
    note = models.CharField(max_length=300)
    dishes = models.ManyToManyField(Dish, through='JoinOrder')


class JoinOrder(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish_order')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
