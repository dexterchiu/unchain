from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from datetime import datetime


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
    occupant = models.ForeignKey('Party', null=True, on_delete=models.SET_NULL)

    def __str__():
        print ("I am a %s capactiy table" % (capactiy))


class Party(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()
    arrival_time = models.DateTimeField(editable=False)
    seat = models.ForeignKey(Table, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        '''overloading save to ensure arrival time is always now'''
        if not self.id:
            self.arrival_time = timezone.now()
        return super(Party, self).save(*args, **kwargs)

    def __str__():
        print ("A party of %s under %s that came in at %s" % (size, name, arrival_time))

def test():
    t1 = Table(capacity=2, occupant=None)
    t2 = Table(capacity=2, occupant=None)
    t3 = Table(capacity=4, occupant=None)
    t4 = Table(capacity=4, occupant=None)
    t5 = Table(capacity=8, occupant=None)
    t6 = Table(capacity=8, occupant=None)
    t1.save()
    print ("Just created a table: " + str(t1))
    t2.save()
    print ("Just created a table: " + str(t2))
    t3.save()
    print ("Just created a table: " + str(t3))
    t4.save()
    print ("Just created a table: " + str(t4))
    t5.save()
    print ("Just created a table: " + str(t5))
    t6.save()
    print ("Just created a table: " + str(t6))

    #fill up all the tables
    p1 = Party(name='Nethaniel', size=2, arrival_time=datetime.now(), seat=None)
    p1.save()
    print ("Just created a party: " + str(p1))
    party_entered(p1)
    print ("This is p1's seat: " + p1.seat)
    p2 = Party(name='Bob', size=4, arrival_time=datetime.now(), seat=None)
    p2.save()
    print ("Just created a party: " + str(p2))
    party_entered(p2)
    print ("This is p2's seat: " + p2.seat)
    p3 = Party(name='Flora', size=8, arrival_time=datetime.now(), seat=None)
    p3.save()
    print ("Just created a party: " + str(p3))
    party_entered(p3)
    print ("This is p3's seat: " + p3.seat)
    p4 = Party(name='Billy', size=2, arrival_time=datetime.now(), seat=None)
    p4.save()
    print ("Just created a party: " + str(p4))
    party_entered(p4)
    print ("This is p4's seat: " + p4.seat)
    p5 = Party(name='Shoyu', size=4, arrival_time=datetime.now(), seat=None)
    p5.save()
    print ("Just created a party: " + str(p5))
    party_entered(p5)
    print ("This is p5's seat: " + p5.seat)
    p6 = Party(name='HelloWorld', size=8, arrival_time=datetime.now(), seat=None)
    p6.save()
    print ("Just created a party: " + str(p6))
    party_entered(p6)
    print ("This is p6's seat: " + p6.seat)

    #create a queue of people waiting for tables
    p7 = Party(name='lalala', size=2, arrival_time=datetime.now(), seat=None)
    p7.save()
    print ("Just created a party: " + str(p7))
    party_entered(p7)
    print ("This is p7's seat: " + p7.seat)
    p8 = Party(name='idkmyname', size=4, arrival_time=datetime.now(), seat=None)
    p8.save()
    print ("Just created a party: " + str(p8))
    party_entered(p8)
    print ("This is p8's seat: " + p8.seat)
    p9 = Party(name='whatsmyname', size=8, arrival_time=datetime.now(), seat=None)
    p9.save()
    print ("Just created a party: " + str(p9))
    party_entered(p9)
    print ("This is p9's seat: " + p9.seat)
    p10 = Party(name='whoami', size=2, arrival_time=datetime.now(), seat=None)
    p10.save()
    print ("Just created a party: " + str(p10))
    party_entered(p10)
    print ("This is p10's seat: " + p10.seat)
    p11 = Party(name='whoareyou', size=4, arrival_time=datetime.now(), seat=None)
    p11.save()
    print ("Just created a party: " + str(p11))
    party_entered(p11)
    print ("This is p11's seat: " + p11.seat)
    p12 = Party(name='iamme', size=2, arrival_time=datetime.now(), seat=None)
    p11.save()
    print ("Just created a party: " + str(p12))
    party_entered(p12)
    print ("This is p12's seat: " + p12.seat)

    #release tables in particular order to test whether parties are seated correctly
    table_freed(t5) #p9 should take this table
    print ("This is the new occupant of t5: " + t5.occupant + " and the actual occupant should be: " + p9)
    table_freed(t3) #p8 should take this table
    print ("This is the new occupant of t3: " + t3.occupant + " and the actual occupant should be: " + p8)
    table_freed(t1) #p7 should take this table
    print ("This is the new occupant of t1: " + t1.occupant + " and the actual occupant should be: " + p7)
    table_freed(t4) #p11 should take this table
    print ("This is the new occupant of t4: " + t4.occupant + " and the actual occupant should be: " + p11)
    table_freed(t6) #p10 should take this table
    print ("This is the new occupant of t6: " + t6.occupant + " and the actual occupant should be: " + p10)
    table_freed(t2) #p12 should take this table
    print ("This is the new occupant of t2: " + t2.occupant + " and the actual occupant should be: " + p12)


if __name__ == '__main__':
    test()