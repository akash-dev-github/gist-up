from __future__ import unicode_literals
import json
from django.contrib.auth.models import User

from django.db import models
import six


def validate_json(value):
    if isinstance(value, six.string_types):
        try:
            value = json.loads(value)
        except ValueError:
            value = json.loads("{}")
        pass


class Article(models.Model):
    title = models.CharField(max_length=128, blank=True, default='')
    tags = models.CharField(max_length=256, blank=True, default='')

    text = models.TextField(blank=True, default='')

    is_active = models.BooleanField(default=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (
            self.title,
            self.tags,
        )


class Reader(models.Model):
    user = models.ForeignKey(User)

    religion = models.CharField(max_length=64, blank=True, default='')
    gender = models.CharField(max_length=64, blank=True, default='')
    interests = models.CharField(max_length=256, blank=True, default='')

    is_active = models.BooleanField(default=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s" % (
            self.religion,
            self.gender,
            self.interests,
        )


class Reaction(models.Model):
    reader = models.ForeignKey(Reader)
    article = models.ForeignKey(Article)

    reaction = models.CharField(max_length=64, blank=True, default='')

    is_active = models.BooleanField(default=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reaction
