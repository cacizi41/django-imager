# -*- coding: utf-8 -*-
"""signal handlers registered by the  imager_users app."""
from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from imager_profile.models import ImagerProfile
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def verify_imager_profile(sender, **kwargs):
    if kwargs.get('created', False):
        try:
            new_profile = ImagerProfile(user=kwargs['instance'])
        except(KeyError, ValueError):
            msg = 'Unable to create ImagerProfile for {}.'
            logger.error(msg.format(kwargs['instance']))


@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def remove_imager_profile(sender, **kwargs):
    try:
        kwargs['insatnce'].profile.delete()
    except (KeyError, AttributeError):
        msg = (
            "ImagerProfile instance not deleted for {}."
            "Perhaps it does no exist?"
        )
        logger.warn(msg.foramt(kwargs['instance']))