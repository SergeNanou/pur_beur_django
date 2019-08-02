from django.test import TestCase
from connect.models import UserProfileInfo
from django.db import models
from django.contrib.auth.models import User
# models test
class UserProfileInfoTest(TestCase):

    def create_user(self, username="AFFOUMOU", password="Python", email="serge.nanou@hetic.net"):
        return (User.objects.create(username=username, password=password, email=email))

    def test_user_creation(self):
        user = self.create_user()
        U = UserProfileInfo(user) 

        self.assertTrue(isinstance(U, UserProfileInfo))
        self.assertEqual(user.__str__(), user.username)