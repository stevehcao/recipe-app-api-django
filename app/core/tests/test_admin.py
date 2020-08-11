from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self):
        # test client
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com', password='Password123')
        # auto login with django auth
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='password123',
            name='Test user full name')

    # these admin:... urls are listed in the django admin DOCS
    def test_users_listed(self):
        """Test that users are listed on user page"""
        # reverse allows you to grab url dynamically
        # type the app:url you want or names for the url
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        # assertContains checks a few different things
        # will check if response has what you pass in and check for status code 200
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/<self.user.id>

        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""

        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

