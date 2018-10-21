from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.




class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Post.objects.create(title='test')

    def test_title_max_length(self):
        post=Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length,200)