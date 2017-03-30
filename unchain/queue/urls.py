# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

app_name = 'queue'
urlpatterns = [
    url(
        regex=r'^parties/$',
        view=views.PartyListView.as_view(),
        name='party_list'
    ),
    url(
        regex=r'^parties/(?P<pk>\d+)$',
        view=views.PartyDetailView.as_view(),
        name='party_detail'
    ),
    url(
        regex=r'^tables/$',
        view=views.TableListView.as_view(),
        name='table_list'
    ),
    url(
        regex=r'^tables/(?P<pk>\d+)$',
        view=views.TableDetailView.as_view(),
        name='table_detail'
    ),
]
