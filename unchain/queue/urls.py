# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^parties/$',
        view=views.PartyListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^tables/$',
        view=views.TableListView.as_view(),
        name='list'
    ),
]
