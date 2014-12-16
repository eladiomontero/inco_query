from django.test import TestCase
from incoquery.models import Contact

# Create your tests here.
class contactTests (TestCase):
    def test_str(self):
        contact = Contact(first_name = "Eladio", last_name = "Montero")
        self.assertEquals(str(contact), "Eladio Montero")