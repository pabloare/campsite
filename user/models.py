from django.db import models
from manager.models import Dish, Seat, Restaurant


class Payment(models.Model):
    wants_to_pay = models.BooleanField(default=False)
    card = models.BooleanField(default=False)
    change_if_cash = models.IntegerField(default=0)
    has_payed = models.BooleanField(default=False)


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant')
    username = models.CharField(max_length=30, default="noUsername")
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE, related_name='seat')
    note = models.CharField(max_length=300)
    dishes = models.ManyToManyField(Dish, through='JoinOrder')
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name="payment")


class JoinOrder(models.Model):
    dishes = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish_order')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
