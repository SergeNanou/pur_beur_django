from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

class IndPageConnexTestCase(TestCase):
    def test_ind_page_connex(self):
        response = self.client.get(reverse('ind_pge_connex'))
        self.assertEqual(response.status_code, 200)
class IndexTestCase(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
class SpecialTestCase(TestCase):
    def test_special(self):
        response = self.client.get('/special/')
        self.assertEqual(response.status_code, 302)

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret',
            'email': 'connect@yahoo.fr'}
        User.objects.create_user(**self.credentials)
    def test_register(self):
        # send register data
        response = self.client.post('/register/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
    def test_login(self):
        # send login data
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        response = self.client.post('/user_login/', self.credentials, follow=True)
        response_1 = self.client.get('/special/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response_1.status_code, 200)
        self.credentials_0 = {
            'username': 'testuse',
            'password': 'secret'}
        response_0 = self.client.post('/user_login/', self.credentials_0, follow=True)
        self.assertEqual(response_0.status_code, 200)
    def test_logout(self):
        # send login data
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        response = self.client.post('/user_login/', self.credentials, follow=True)
        # Log out
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('reception'))
        self.assertEqual(response.status_code, 200)
class loginTestCase(TestCase):
    def test_login_pge(self):
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)



        
       

        
       
        
