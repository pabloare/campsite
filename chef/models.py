from django.db import models
from manager.models import Restaurant


class Chef(models.Model):
    chef_id = models.CharField(max_length=70, default="")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='chef')
    accumulator = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.chef_id
