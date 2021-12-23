from django.test import TestCase


class TestStringMethods(TestCase):
    def test_length(self):
        self.assertEqual(len('yatube'), 6)
