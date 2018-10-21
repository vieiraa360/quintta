from django.test import TestCase
from .models import Product
from django.test import Client

# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Post models
    """
    
    def test_str(self):
        test_name = Product(name='A product')
        self. assertTrue(str(test_name), 'A product')

    def test_view_url_exists_at_desired_location(self):
    	response = self.client.get("/products/")
    	self.assertTrue(response.status_code, 200)