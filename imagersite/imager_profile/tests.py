"""Test profile model."""
from __future__ import unicode_literals
# from django.conf import settings
from django.test import TestCase
from django.db.models import QuerySet, Manager
from django.contrib.auth.models import User
from .models import ImagerProfile
# import factory


class TestProfile(TestCase):

    def setUp(self):
        self.test_user_1 = User.objects.create_user(username='user1',
                                                    email='user1@email.com',
                                                    password='password1')
        self.test_user_2 = User.objects.create_user(username='user2',
                                                    email='user2@email.com',
                                                    password='password2')

    def test_user_created(self):
        """Test users created successfully."""
        self.assertEquals(len(User.objects.all()), 2)

    def test_profile_created(self):
        """Test profils created automatically after user created."""
        self.assertEquals(len(ImagerProfile.objects.all()), 2)

    def test_profile_user(self):
        """Test user in profile is the user."""
        self.assertEquals(ImagerProfile.objects.all()[0], self.test_user_1.profile)

    def test_user_profile_deleted(self):
        """Test when user is deleted, profile is deleted too."""
        self.assertEquals(len(ImagerProfile.objects.all()), 2)
        self.test_user_1.delete()
        self.assertEquals(len(ImagerProfile.objects.all()), 1)
        self.assertEquals(ImagerProfile.objects.all()[0], self.test_user_2.profile)

    def test_profile_deleted_only(self):
        """Test user will not be deleted when only profile deleted."""
        self.assertEquals(len(User.objects.all()), 2)
        self.assertEquals(len(ImagerProfile.objects.all()), 2)
        self.test_user_1.profile.delete()
        self.assertEquals(len(ImagerProfile.objects.all()), 1)
        self.assertEquals(len(User.objects.all()), 2)

    def test_profile_active(self):
        """Test profile is active."""
        self.assertEquals(self.test_user_1.profile.is_active, True)
        # is_active(), return bool, not callable

    def test_active_profile(self):
        """Test how many active profile exist."""
        self.assertEquals(ImagerProfile.active.count(), 2)

    def test_add_followers(self):
        """Test followers can be added in one direction."""
        self.test_user_1.profile.followers.add(self.test_user_2)
        # self.assertEquals(self.test_user_1.profile.followers.count(), 1)
        # self.assertEquals(self.test_user_2.profile.followers.count(), 0)
        # self.assertEquals(self.test_user_2.profile.follower_of.all()[0],
        #                   self.test_user_1.profile)
