from __future__ import unicode_literals, absolute_import
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class Party(models.Model):
	name = models.CharField(max_length=255)
	size = models.IntegerField(default=0)
	def __str__(self):
		return self.name

	def __init__(self, name, size):
		self.name = name
		self.size = size
