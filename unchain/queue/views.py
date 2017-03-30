from django.views.generic import DetailView, ListView

from .models import Party, Table

# Create your views here.


class PartyListView(ListView):
    model = Party
    template_name = 'queue/party_list.html'
    context_object_name = 'party_list'


class PartyDetailView(DetailView):
    model = Party
    template_name = 'queue/party_detail.html'


class TableListView(ListView):
    model = Table
    template_name = 'queue/table_list.html'
    context_object_name = 'table_list'


class TableDetailView(DetailView):
    model = Table
    template_name = 'queue/table_detail.html'
