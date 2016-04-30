# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# from django.contrib.auth.models import User


PHOTO_TYPES = [
    ('advertising', 'Advertising'),
    ('architecture', 'Architecture'),
    ('book', 'Book'),
    ('deeper perspective', 'Deeper Perspective'),
    ('editorial', 'Editorial'),
    ('event', 'Event'),
    ('fine art', 'Fine Art'),
    ('moving images', 'Moving Images'),
    ('nature', 'Nature'),
    ('people', 'People'),
    ('special', 'Special')
]

PRIVACY_SETTING = [
    ('private', 'Private'),
    ('public', 'Public'),
    ('shared', 'Shared')
]


DATE_FORMAT = '%d %B %Y %I:%M%p'


@python_2_unicode_compatible
class Photo(models.Model):
    """Photo attributes."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='photo',
        null=True, blank=True
    )
    title = models.CharField(default='', max_length=128, null=True, blank=True)
    description = models.TextField(default='', max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=128, choices=PHOTO_TYPES)
    img_file = models.ImageField(upload_to='img_file')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    privacy = models.CharField(max_length=128, choices=PRIVACY_SETTING, default='Public')
    # in_album = md.ManyToManyField('Album', related_name='photos')

    def __str__(self):
        """String output of photo instance."""
        return self.title


@python_2_unicode_compatible
class Album(models.Model):
    """Collection of photoes in database."""

    album_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='album',
        null=True
    )
    album_title = models.CharField(max_length=255, null=True, blank=True)
    album_description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    contain_photo = models.ManyToManyField('Photo', related_name='albums')
    privacy = models.CharField(max_length=128, choices=PRIVACY_SETTING, default='Public')

    def __str__(self):
        """String output of photo instance."""
        return self.album_title
