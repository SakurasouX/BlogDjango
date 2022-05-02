from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100, default=f'Title{id}')
    content = models.TextField(null=True)
    pub_date = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
