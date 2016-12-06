from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Table(models.Model):
    TWO_SEATER = 2
    FOUR_SEATER = 4
    EIGHT_SEATER = 8
    CAPACITY_CHOICES = (
        (TWO_SEATER, 'two seater'),
        (FOUR_SEATER, 'four seater'),
        (EIGHT_SEATER, 'eight seater'),
    )
    capacity = models.IntegerField(choices=CAPACITY_CHOICES, default=TWO_SEATER)
    occupied = models.BooleanField(default=False)

    def is_occupied(self):
        return self.occupied


class Party(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()
