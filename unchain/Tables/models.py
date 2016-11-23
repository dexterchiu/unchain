from __future__ import unicode_literals, absolute_import
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from Queues import models

@python_2_unicode_compatible
class TwoPersonTable(models.Model):
	occupied = models.BooleanField(default=False)
	two_person_queue = Queues
	
	def __str__(self):
		return "Two Person Table"

	def __init__(self, occupied, two_person_queue):
		self.occupied = occupied
		self.two_person_queue = two_person_queue

	def setOccupied(self, occupied):
		self.occupied = occupied

	def checkOccupied(self):
		return self.occupied

@python_2_unicode_compatible
class FourPersonTable(TwoPersonTable):
	occupied = models.BooleanField(default=False)
	four_person_queue = Queues

	def __str__(self):
		return "Four Person Table"

	def __init__(self, occupied, two_person_queue, four_person_queue):
		super(FourPersonTable, self).__init__(occupied, two_person_queue)
		self.four_person_queue = four_person_queue

	def setOccupied(self, occupied):
		super(FourPersonTable, self).setOccupied(occupied)

	def checkOccupied(self):
		return self.occupied

@python_2_unicode_compatible
class EightPersonTable(FourPersonTable):
	occupied = models.BooleanField(default=False)
	eight_person_queue = Queues

	def __str__(self):
		return "Eight Person Table"

	def __init__(self, occupied, two_person_queue, four_person_queue, eight_person_queue):
		super(EightPersonTable, self).__init__(occupied, two_person_queue, four_person_queue)
		self.eight_person_queue = eight_person_queue

	def setOccupied(self, occupied):
		super(EightPersonTable, self).setOccupied(occupied)

	def checkOccupied(self):
		return self.occupied