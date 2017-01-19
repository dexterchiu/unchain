from django.test import TestCase
from django.core.exceptions import MultipleObjectsReturned

from queue.models import Table, Party


# Create your tests here.
# model unit tests
class TableTestCase(TestCase):
    def setUp(self):
        Table.objects.create()
        Table.objects.create(capacity='two seater')
        Table.objects.create(capacity='four seater')
        Table.objects.create(capacity='eight seater')

    def test_table_capacities(self):
        table_for_eight = Table.objects.get(capacity='eight seater')
        table_for_four = Table.objects.get(capacity='four seater')
        self.assertEqual(table_for_four.capacity, 4)
        self.assertEqual(table_for_eight.capacity, 8)

    def test_table_default(self):
        # two tables of two were created as the default creates a two seater
        with self.assertRaises(MultipleObjectsReturned):
            table_for_two = Table.objects.get(capacity='two seater')
            self.fail("Got one table: {}".format(table_for_two))


class PartyTestCase(TestCase):
    def setUp(self):
        Party.objects.create()
