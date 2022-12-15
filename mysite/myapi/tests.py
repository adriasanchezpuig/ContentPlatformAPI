from django.test import TestCase
from io import StringIO
from django.core.management import call_command
from django.test import SimpleTestCase, TestCase
from myapi.management.commands.compute_ratings import Command

# Create your tests here.

class ComputeRatingsTests(SimpleTestCase):

    def test_calculate_means(self):
        test = {
            "Movies":[1,2,3],
            "Music":[3,4,5]
            }
        success = {
            "Movies":2,
            "Music": 4
        }
        result = Command().calculate_channel_means(test)
        self.assertEqual(result, success)
    
    def test_order_ratings(self):
        test = {
            "Movies":2,
            "Music": 4
        }
        success = [
            ("Music", 4),
            ("Movies", 2)
        ]
        result = Command().order_ratings(test)
        self.assertEqual(result, success)
