from django.db import models
from manager.models import Restaurant, Dish


class Chef(models.Model):
    chef_id = models.CharField(max_length=70, default="")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='chef')
    accumulator = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    dishes = models.ManyToManyField(Dish, through='Join')

    def __str__(self):
        return self.chef_id


class Join(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish_chef')
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name='chef')
