# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# from django.db.models.signals import post_save
from django.contrib.auth.models import User


class ActiveProfile(models.Manager):
    """Returns only active profiles."""

    def get_queryset(self):
        """Return queryset on activate profile."""
        query = super(ActiveProfile, self).get_queryset()
        return query.filter(user__is_active__exact=True)


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

US_REGIONS = [
    ('pnw', 'Pacific Northwest'),
    ('ne', 'New England'),
    ('ma', 'Mid-Atlantic'),
    ('se', 'Southeast'),
    ('mw', 'Midwest'),
    ('ds', 'Deep South'),
    ('sw', 'Southwest'),
    ('cf', 'California'),
    ('ak', 'Alaska'),
    ('hi', 'Hawaii')
]


@python_2_unicode_compatible
class ImagerProfile(models.Model):
        user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            related_name='profile'
        )
        camera_model = models.CharField(max_length=255)
        type_of_photography = models.CharField(
            max_length=128,
            choices=PHOTO_TYPES,
        )
        friends = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name='friend_of'
        )
        region = models.CharField(
            max_length=3,
            choices=US_REGIONS
        )
        objects = models.Manager()
        active = ActiveProfile()

        def __str__(self):
            """String output of profile model."""
            return "Imager profile for {}".format(self.user)

        @property
        def is_active(self):
            """Return a boolean value indicating whether the user profile is active."""
            return self.user.is_active
