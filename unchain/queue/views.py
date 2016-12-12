from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.list import MultipleObjectMixin


# Create your views here.

class QueueView(MultipleObjectMixin, ListView):
    pass
