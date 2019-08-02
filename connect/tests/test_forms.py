from django.test import TestCase
from connect.forms import UserForm
from django.contrib.auth.models import User

class formTestCase(TestCase):

    def test_valid_form(self):
        
       
        data = {'username': 'serge', 'password': 'akas', 'email': 'connect_1@yahoo.fr',}
        form = UserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        
        
        data = {'username': '', 'password': '', 'email':'',}
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())
