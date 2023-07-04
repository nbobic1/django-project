from django.db import models

from core.models import User


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, null=False)
    description = models.CharField(max_length=555, blank=True, null=True)
    url = models.FileField(upload_to='content', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True, related_name='posts')


class Content(models.Model):
    url = models.FileField(upload_to='content', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    style = models.TextField(blank=True, null=True)
    type = models.IntegerField()
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, null=True, blank=True, related_name='content')