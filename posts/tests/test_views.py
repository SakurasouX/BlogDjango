from django.test import TestCase
from django.contrib.auth.models import User

from posts.models import Post


def create_user():
    user = User.objects.create_user(username='John', password='secret')
    return user


def create_post():
    user = create_user()
    post = Post.objects.create(
        title='title',
        content='content',
        user=user
    )
    return post


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """Home page loading test """
        response = self.client.get('/posts/')
        redirect = self.client.get('/')
        self.assertEqual(redirect.status_code, 301)
        self.assertEqual(response.status_code, 200)

    def test_detail_loads_properly(self):
        """Post detail page loading test"""
        post = create_post()
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

    def test_post_create(self):
        """Testing the creation of a post on a page"""
        user = create_user()
        self.client.login(username='John', password='secret')

        data = {
            'title': 'title',
            'content': 'content',
            'user': 'user'
        }

        response = self.client.post('/posts/create', data)
        post = Post.objects.get(id=1)
        self.assertEqual(response.url, '/')
        self.assertEqual(post.title, 'title')
        self.assertEqual(post.content, 'content')
        self.assertEqual(post.user, user)

    def test_update_loads_property_without_posts(self):
        """Testing the post update page without posts"""
        response = self.client.get('/posts/9999/update')
        self.assertEqual(response.status_code, 404)

    def test_update_loads_property_with_post(self):
        """Testing the post update page with posts"""
        post = create_post()
        post.save()
        self.client.login(username='John', password='secret')
        response = self.client.get(f'/posts/{post.id}/update')
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        """Testing the update of a post by NOT the author of the post"""
        post = create_post()
        post.save()
        response = self.client.get(f'/posts/{post.id}/update')
        self.assertEqual(response.status_code, 403)

    def test_update_post_with_author(self):
        """Testing the update of a post by the author of the post"""
        post = create_post()
        post.save()
        self.client.login(username='John', password='secret')
        response = self.client.get(f'/posts/{post.id}/update')
        self.assertEqual(response.status_code, 200)

        data = {
            'title': 'another_title',
            'content': 'another_content'
        }

        response = self.client.post(f'/posts/{post.id}/update', data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'another_title')
        self.assertEqual(post.content, 'another_content')
        user = User.objects.get(id=1)
        self.assertEqual(post.user, user)

    def test_delete_post(self):
        """Testing the deletion of a post by NOT the author"""
        post = create_post()
        response = self.client.get(f'/posts/{post.id}/delete')
        self.assertEqual(response.status_code, 403)

    def test_delete_post_with_author(self):
        """Testing the deletion of a post by the author"""
        post = create_post()
        self.client.login(username='John', password='secret')
        response = self.client.get(f'/posts/{post.id}/delete')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        