from __future__ import unicode_literals, absolute_import
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from Parties import models
from django.contrib.postgres.fields.array import ArrayField

@python_2_unicode_compatible
class TwoPersonQueue(models.Model):
	list_of_parties = ArrayField(Party)
	def __str__(self):
		return "Two Person Queue"

	def __init__(self):
		list_of_parties = []

	def appendParties(self, party):
		self.list_of_parties.append(party)

	def removeParty(self):
		self.list_of_parties.pop(0)

@python_2_unicode_compatible
class FourPersonQueue(models.Model):
	list_of_parties = ArrayField(Party)
	def __str__(self):
		return "Four Person Queue"

	def __init__(self):
		list_of_parties = []

	def appendParties(self, party):
		self.list_of_parties.append(party)

	def removeParty(self):
		self.list_of_parties.pop(0)	

@python_2_unicode_compatible
class EightPersonQueue(models.Model):
	list_of_parties = ArrayField(Party)
	def __str__(self):
		return "Eight Person Queue"

	def __init__(self):
		list_of_parties = []

	def appendParties(self, party):
		self.list_of_parties.append(party)

	def removeParty(self):
		self.list_of_parties.pop(0)