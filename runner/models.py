from django.db import models
from manager.models import Restaurant


class Runner(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='runner')
    runner_id = models.CharField(max_length=70, default="")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.runner_id
