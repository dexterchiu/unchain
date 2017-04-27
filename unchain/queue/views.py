from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from django.urls import reverse

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


def party_leave(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    try:
        party.leave_table()
        party.delete()
    except IntegrityError:
        return render(request, 'queue/party_detail.html', {
            'party': party,
            'error_message': 'Error, party cannot leave due to database error'
        })
    else:
        return HttpResponseRedirect(reverse(
            'queue:party_list',
        ))


def fill_table(request, table_id):
    table = get_object_or_404(Table, pk=table_id)
    try:
        table.fill_table()
    except IntegrityError:
        return render(request, 'queue/table_detail.html', {
            'table': table,
            'error_message': 'Error, table cannot be filled due to database error'
        })
    else:
        return HttpResponseRedirect(reverse(
            'queue:table_detail',
            args=(table.id,)
        ))
