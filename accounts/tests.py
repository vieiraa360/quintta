from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from .models import UserProfile
from .forms import UserRegistrationForm
from .forms import UserLoginForm
from django.test import Client
from django.conf import settings
from .forms import *

# Create your tests here.

class CustomUserTest(TestCase):

    def test_registration_form(self):
        form = UserRegistrationForm({
            'username': 'testuser',
            'email': 'user@example.com',
            'password1': 'password1',
            'password2': 'password1',
        })
 
        self.assertFalse(form.is_valid())
    
    def test_registration_form_fails_with_missing_password(self):
        form = UserRegistrationForm({
            'username': 'testuser',
            'email': 'user@example.com',
            'password1': 'password1',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                "please enter both passwords",
                                form.full_clean())


    def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'username': 'testuser',
            'email': 'user@example.com',
            'password1': 'password1',
            'password2': 'password2',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
form.full_clean())


class UserProfile_Test(TestCase):
    def test_details(self):
        response = self.client.get('/accounts/profile/')
        self.assertTrue(response.status_code, 200)
        
    def test_index(self):
            response = self.client.get('/')
            self.assertTrue(response.status_code, 200)

        
class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@example.com", password="user", first_name="John", lastname="Smith")

class UserForm_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserForm(data={'email': "user@example.com", 'password': "user", 'first_name': "John", 'last_name': "Smith"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = UserForm(data={'email': "", 'password': "mp", 'first_name': "mp", 'phone': ""})
        self.assertTrue(form.is_valid())