from django.test import TestCase
from django.contrib.auth.models import User

from posts.models import Post


class PostModelTest(TestCase):
    def test_post_create(self):
        """Creating post with user and test his"""
        user = User.objects.create_user('John')
        post = Post.objects.create(
            title='title',
            content='content',
            user=user
        )
        post.save()

        self.assertEqual('title', post.title)
        self.assertEqual('content', post.content)
        self.assertEqual(user, post.user)
