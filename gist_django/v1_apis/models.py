from __future__ import unicode_literals
import json

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

    def __unicode__(self):
        return "%s %s" % (
            self.title,
            self.tags,
        )
