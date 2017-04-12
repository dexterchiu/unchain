from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


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
    # use quotes to force a lazy reference
    # might want to consider switching to a one-to-one relation instead

    def fill_table(self):
        '''
        if table is filled, do nothing
        if table is empty, select appropriate party and fill table
        if table is empty and no appropriate party is available, do nothing
        '''
        try:
            party = Party.objects.filter(
                size__gte=self.capacity
            ).filter(
                seat__isnull=True
            ).order_by(
                'arrival_time'
            )[0:1].get()
            party.seat = self
            party.save()

        except ObjectDoesNotExist:
            print('No suitable parties to fill table')

    def __str__(self):
        try:
            return str("Table {} of capacity {}, occupant: {}".format(
                self.id,
                self.capacity,
                self.party,
            ))
        except ObjectDoesNotExist:
            return str("Table {} of capacity {}, unoccupied".format(
                self.id,
                self.capacity,
            ))


class Party(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()
    arrival_time = models.DateTimeField(editable=False)
    seat = models.OneToOneField(
        Table,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def save(self, *args, **kwargs):
        '''overloading save to ensure arrival time is always now'''
        if not self.id:
            self.arrival_time = timezone.now()
        return super(Party, self).save(*args, **kwargs)

    def leave_table(self):
        '''
        sets seat to none, indicating the party has left the table
        '''
        self.seat = None
        self.save()

    def __str__(self):
        return str("{}'s party of {}, arrived @ {}".format(self.name,
                                                           self.size,
                                                           self.arrival_time))

    class Meta:
        verbose_name_plural = 'parties'
