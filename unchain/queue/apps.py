from __future__ import unicode_literals

from django.apps import AppConfig


class QueueConfig(AppConfig):
    name = 'unchain.queue'
    verbose_name = "Queue"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
