from django.db import models
from manager.models import Restaurant, Dish
from user.models import Order


class Chef(models.Model):
    chef_id = models.CharField(max_length=70, default="")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='chef')
    accumulator = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    dishes = models.ManyToManyField(Dish, through='Join')

    def __str__(self):
        return self.chef_id


class Join(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='join_restaurant')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish_chef')
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name='chef')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='dish_order')
    # Added fields
    note = models.CharField(max_length=300)
    ready = models.BooleanField(default=False)
