from django.views.generic import ListView

from .models import Party, Table

# Create your views here.


class PartyListView(ListView):
    model = Party


class TableListView(ListView):
    model = Table
