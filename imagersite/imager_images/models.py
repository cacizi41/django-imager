# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


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
    ('public', 'Public')
]


class Photo(models.Model):
    owner = models.CharFiels(max_length=128)
    title = models.CharFiels(max_length=128)
    genre = models.CharFiels(max_length=128, choices=PHOTO_TYPES)
    privacy = models.CharFiels(max_length=128, choices=PRIVACY_SETTINGG)
    file = models.ImageField



class Album(models.Model):
    album_name = models.CharFiels(max_length=255)
    creat_date = models.DateField()

