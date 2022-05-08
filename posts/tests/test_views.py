from django.test import TestCase
from django.contrib.auth.models import User

from posts.models import Post


def create_user():
    user = User.objects.create_user(username='John', password='secret')
    user.save()
    return user


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """Home page loading test """
        response = self.client.get('/posts/')
        redirect = self.client.get('/')
        self.assertEqual(redirect.status_code, 301)
        self.assertEqual(response.status_code, 200)

    def test_detail_loads_properly(self):
        """Post detail page loading test"""
        user = create_user()
        post = Post.objects.create(
            title='title',
            content='content',
            user=user
        )
        post.save()
        response = self.client.get(f'/posts/{post.id}')
        response_error = self.client.get('posts/1000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_error.status_code, 404)

    def test_create_loads_login(self):
        """Testing the post creation page with login user"""
        user = create_user()
        self.client.login(username='John', password='secret')
        response = self.client.get('/posts/create')
        self.assertEqual(response.status_code, 200)

    def test_create_loads_properly_logout(self):
        """Testing the post creation page without login user"""
        redirect = self.client.get('/posts/create')
        self.assertEqual(redirect.url, '/accounts/login/?next=/posts/create')
        self.assertEqual(redirect.status_code, 302)
