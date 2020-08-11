from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
# make it more human readable
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


# dynamic list of arguments of keys and values
def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


# public is just personal perference
# public vs private
# public is unauthenticated user and private is already authenticated
class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating using with a valid payload is successful"""
        payload = {
            'email': 'klaythompson@warriors.com',
            'password': '3ptsandD',
            'name': 'name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # unwind the response for this
        # created user object is return so if you do **res.data...
        # it will take dictionary response (with id field) will look similar to payload
        # if you are able to get it from the object that it will work
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        # check that password field is not in res.data
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating a user that already exists fails"""
        payload = {
            'email': 'klaythompson@warriors.com',
            'password': '3ptsandD',
            'name': 'Klay Thompson',
        }
        # **payload,  email='klaythompson@warriors.com', password='3ptsandD'
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that password must be more than 5 characters"""
        # every test refreshes new test database
        # payload needs name key because is needed for the model
        payload = {
            'email': 'test@londonappdev.com',
            'password': 'pw',
            'name': 'Test'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        # checks in the model if email exists it should NOT exist
        user_exists = get_user_model().objects.filter(
            email=payload['email']).exists()
        self.assertFalse(user_exists)
