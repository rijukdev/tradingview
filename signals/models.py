from django.db import models
from django.utils import timezone


class Signals(models.Model):
    market = models.CharField(max_length=10)
    broken = models.CharField(max_length=10)
    asset = models.CharField(max_length=10)
    entry = models.CharField(max_length=10)
    direction = models.CharField(max_length=10)
    active = models.CharField(max_length=1)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.asset
