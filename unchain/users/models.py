# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

@python_2_unicode_compatible
class Party(models.Model):
	name = models.CharField(max_length=255)
	size = models.IntegerField(default=0)
	def __str__(self):
		return self.name

	def __init__(self, name, size):
		self.name = name
		self.size = size

@python_2_unicode_compatible
class TwoPersonQueue(models.Model):
	list_of_parties = []
	def __str__(self):
		return "Two Person Queue"

	def __init__(self, party):
		list_of_parties.append(party)

	def appendParties(party):
		list_of_parties.append(party)

@python_2_unicode_compatible
class FourPersonQueue(models.Model):
	list_of_parties = []
	def __str__(self):
		return "Four Person Queue"

	def __init__(self, party):
		list_of_parties.append(party)

	def appendParties(party):
		list_of_parties.append(party)

@python_2_unicode_compatible
class EightPersonQueue(models.Model):
	list_of_parties = []
	def __str__(self):
		return "Eight Person Queue"

	def __init__(self, party):
		list_of_parties.append(party)

	def appendParties(party):
		list_of_parties.append(party)

@python_2_unicode_compatible
class TwoPersonTable(models.Model):
	occupied = models.BooleanField(default=false)
	
	def __str__(self):
		return "Two Person Table"

	def __init__(self, occupied, two_person_queue):
		self.occupied = occupied
		self.two_person_queue = two_person_queue

@python_2_unicode_compatible
class FourPersonTable(TwoPersonTable):
	occupied = models.BooleanField(default=false)

	def __str__(self):
		return "Four Person Table"

	def __init__(self, occupied, two_person_queue, four_person_queue):
		super(FourPersonTable, self).__init__(occupied, two_person_queue)
		self.four_person_queue = four_person_queue

@python_2_unicode_compatible
class EightPersonTable(FourPersonTable):
	occupied = models.BooleanField(default=false)

	def __str__(self):
		return "Eight Person Table"

	def __init__(self, occupied, two_person_queue, four_person_queue, eight_person_queue):
		super(EightPersonTable, self).__init__(occupied, two_person_queue, four_person_queue)
		self.eight_person_queue = eight_person_queue