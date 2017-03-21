from django.views.generic import ListView

from .models import Party, Table

# Create your views here.


class PartyListView(ListView):
    model = Party
    template_name = 'queue/party_list.html'
    context_object_name = 'party_list'


class TableListView(ListView):
    model = Table
    template_name = 'queue/table_list.html'
    context_object_name = 'table_list'
