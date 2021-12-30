from django.test import TestCase


class TestStringMethods(TestCase):
    def test_length(self):
        self.assertEqual(len('NotTwitter'), 10)
