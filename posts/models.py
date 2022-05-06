from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, default=f'Title')
    content = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
