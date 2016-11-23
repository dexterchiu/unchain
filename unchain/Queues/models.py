from __future__ import unicode_literals, absolute_import
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class TwoPersonQueue(models.Model):
	list_of_parties = []
	def __str__(self):
		return "Two Person Queue"

	def __init__(self, party):
		self.list_of_parties.append(party)

	def appendParties(self, party):
		self.list_of_parties.append(party)

	def removeParty(self):
		self.list_of_parties.pop(0)

@python_2_unicode_compatible
class FourPersonQueue(models.Model):
	list_of_parties = []
	def __str__(self):
		return "Four Person Queue"

	def __init__(self, party):
		self.list_of_parties.append(party)

	def appendParties(self, party):
		self.list_of_parties.append(party)

	def removeParty(self):
		self.list_of_parties.pop(0)	

@python_2_unicode_compatible
class EightPersonQueue(models.Model):
	list_of_parties = []
	def __str__(self):
		return "Eight Person Queue"

	def __init__(self, party):
		self.list_of_parties.append(party)

	def appendParties(self, party):
		self.list_of_parties.append(party)

	def removeParty(self):
		self.list_of_parties.pop(0)