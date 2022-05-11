from django.test import TestCase
from django.contrib.auth.models import User

from posts.models import Post, Comment


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


class PostModelTest(TestCase):
    def test_post_create(self):
        """Creating post with user and test his"""
        post = create_post()
        post.save()
        self.assertEqual('title', post.title)
        self.assertEqual('content', post.content)
        self.assertEqual(post.user, post.user)


class CommentModelTest(TestCase):
    def test_comment_create(self):
        """Creating comments on some post and test his"""
        post = create_post()
        comment = Comment.objects.create(
            user=post.user,
            post=post,
            content='Hello!'
        )
        self.assertEqual('Hello!', comment.content)
        self.assertEqual(post.user, comment.user)
        self.assertEqual(post, comment.post)
