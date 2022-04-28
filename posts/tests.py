from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Post


def create_post(title, content, pub_date):
    return Post.objects.create(title=title, content=content, pub_date=pub_date)


class PostModelTest(TestCase):

    def test_no_post(self):
        response = self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Not found posts')
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_post_model(self):
        post_time = timezone.now()
        post = create_post('TestTitle', 'TestContent', post_time)
        self.assertEqual(post.title, 'TestTitle')
        self.assertEqual(post.content, 'TestContent')
        self.assertEqual(post.pub_date, post_time)

    def test_two_and_more_posts(self):
        post_1 = create_post('Title1', 'Context1', timezone.now())
        post_2 = create_post('Title2', 'Context2', timezone.now())
        response = self.client.get(reverse('posts:index'))
        queryset = response.context['posts']
        self.assertQuerysetEqual(list(queryset), [post_1, post_2])
