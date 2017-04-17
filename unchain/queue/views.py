from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Party, Table

from django.shortcuts import render_to_response, render
from django.template import RequestContext, Context, loader
from django.http import HttpResponse
from django.core.files import File

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


def party_leave(request, party_id):
    party = get_object_or_404(Party, party_id)
    party.leave_table()


def fill_table(request, table_id):
    table = get_object_or_404(Table, table_id)
    table.fill_table()