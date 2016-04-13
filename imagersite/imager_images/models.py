# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


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

PRIVACY_SETTINGG = [
    ('private', 'Private'),
    ('public', 'Public'),
    ('shared', 'Shared')
]# 1st in db, 2nd dispaly


DATE_FORMAT = '%d %B %Y %I:%M%p'

@python_2_unicode_compatible
class Photo(models.Model):
    """Photo attributes."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='photo',
    )
    title = models.CharField(max_length=128)
    description = models.TextField()
    genre = models.CharField(max_length=128, choices=PHOTO_TYPES)
    image = models.ImageField()# upload_to='photo_file'
    date_uploaded = models.DateTimeField(auto_now_add=True)
    privacy = models.CharField(max_length=128, choices=PRIVACY_SETTINGG)

    def __str__(self):
        """String output of photo instance."""
        return self.title


@python_2_unicode_compatible
class Album(models.Model):
    """Collection of photoes in database."""
    album_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        # if user deleted,delete album too.
        related_name='album',
    )
    album_cover = models.ForeignKey(
        'Photo',
        related_name='covered_albums',
    )
    album_title = models.CharField(max_length=255)
    album_description = models.TextField()
    date_created = models.DateTimeField()

    def __str__(self):
        """String output of photo instance."""
        return self.album_title

    # def set_cover(self, photo):
    #     """Set selected photo as album cover."""

    # def owned_photos(self, photos):

    # def add_photos(self, photo):