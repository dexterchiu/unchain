from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.list import MultipleObjectMixin


# Create your views here.

class QueueView(MultipleObjectMixin, ListView):
    pass

    def table_freed(table):
    	table.occupant.delete()
    	table.occupant = None
    	try:
    		available =  party in Party.objects.filter(size <= table.capacity).order_by(-size).order_by(arrival_time)[0]:
    		table.occupant = party
    	except IndexError:
    		table.occupant = None

    def party_entered(party):
    	try:
    		available = table in Table.objects.all().filter(occupant == None, capacity >= party.size).order_by(capacity)[0]
    		party.seat = available
    	except IndexError:
    		party.seat = None