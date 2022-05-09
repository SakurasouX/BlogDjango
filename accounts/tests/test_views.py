from django.test import TestCase
from django.contrib.auth.models import User


def create_user():
    user = User.objects.create_user(username='John', password='secret')
    return user


class ViewsTestCase(TestCase):
    def test_user_login(self):
        """Login page testing"""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'John',
            'password': 'secret'
        }
        user = create_user()
        response = self.client.post('/accounts/login/', data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/posts/')

    def test_user_logout(self):
        """Testing user logout page"""
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)

        user = create_user()
        self.client.login(username='John', password='secret')
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.url, '/posts/')

    def test_registrations(self):
        """Signup page testing and creating new user"""
        response = self.client.get('/accounts/registration/')
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'John',
            'first_name': 'John',
            'last_name': 'Williams',
            'email': 'john@email.com',
            'password': 'secret',
            'password_confirm': 'secret'
        }

        response = self.client.post('/accounts/registration/', data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/posts/')

        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'John')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Williams')
        self.assertEqual(user.email, 'john@email.com')

    def test_personal_cabinet(self):
        """Testing loading personal cabinet page"""
        response = self.client.get('/accounts/personal_cabinet/')
        self.assertEqual(response.status_code, 200)

    def test_password_change(self):
        """Testing the password change page with a valid password"""
        response = self.client.get('/accounts/password_change/')
        self.assertEqual(response.status_code, 200)

        user = create_user()
        self.client.login(username='John', password='secret')

        data = {
            'user_password': 'secret',
            'password1': 'secret1',
            'password2': 'secret1'
        }

        response = self.client.post('/accounts/password_change/', data)
        user = User.objects.get(id=1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/posts/')
        self.assertEqual(user.check_password('secret1'), True)

    def test_password_change_error(self):
        """Testing the password change page with an invalid password"""
        user = create_user()
        self.client.login(username='John', password='secret')

        data = {
            'user_password': 'secret',
            'password1': 'secret1',
            'password2': 'secret2'
        }

        response = self.client.post('/accounts/password_change/', data)
        user = User.objects.get(id=1)
        self.assertEqual(user.check_password('secret'), True)
