# -*- coding: utf-8 -*-
from django.db.models.fields.files import ImageFieldFile
from django.test import TestCase, override_settings
from .models import Photo, Album, PRIVACY_SETTING
from django.conf import settings
from django.contrib.auth.models import User
import factory
import random

TEMP_MEDIA_ROOT = '/tmp/media/'


class UserFactory(factory.django.DjangoModelFactory):
    """Create Users."""

    class Meta:

        model = settings.AUTH_USER_MODEL
        django_get_or_create = ('username',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    username = factory.LazyAttribute(
        lambda obj: ''.join((obj.first_name, obj.last_name)))
    password = factory.PostGenerationMethodCall('set_password', 'password')


class PhotoFactory(factory.django.DjangoModelFactory):
    """Create Photos."""

    class Meta:
        model = Photo

    title = factory.Faker('sentence')
    user = factory.SubFactory(UserFactory, username='factoryuser')
    img_file = factory.django.ImageField()
    privacy = random.choice(PRIVACY_SETTING)


class AlbumFactory(factory.django.DjangoModelFactory):
    """Create Albums."""

    class Meta:
        model = Album

    album_title = factory.Faker('sentence')
    album_description = factory.Faker('sentence')
    privacy = random.choice(PRIVACY_SETTING)
    album_owner = factory.SubFactory(UserFactory, username='factoryuser')


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class Photo(TestCase):
    """Test photo instance."""

    def setUp(self):
        """Initiate Photo instance."""
        self.instance = PhotoFactory.create()

    def test_empty_album(self):
        """Test Photo has no albums."""
        self.assertFalse(self.instance.albums.count())

    def test_img_file_exists(self):
        """Test img_file exists."""
        self.assertTrue(self.instance.img_file)

    def test_img_file_type(self):
        """Test img file type correct."""
        self.assertIsInstance(self.instance.img_file, ImageFieldFile)

    def test_privacy(self):
        """Test published generated."""
        self.assertTrue(self.instance.privacy)

@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class Album(TestCase):
    """Test Album instance."""

    def setUp(self):
        """Initiate Album."""
        self.instance = AlbumFactory.create()

    def test_user(self):
        """Test owner generated."""
        self.assertTrue(self.instance.album_owner)

    def test_title(self):
        """Test title generated."""
        self.assertTrue(self.instance.album_title)

    def test_description(self):
        """Test description generated."""
        self.assertTrue(self.instance.album_description)

    def test_empty_album(self):
        """Test album has no photos."""
        self.assertFalse(self.instance.contain_photo.count())

    def test_privacy(self):
        """Test published generated."""
        self.assertTrue(self.instance.privacy)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class PhotosAlbum(TestCase):
    """A Lot of photos, one album."""

    def setUp(self):
        """Create photos and albums."""
        self.photos = PhotoFactory.create_batch(50)
        self.album1 = AlbumFactory.create()
        self.album2 = AlbumFactory.create()

        for photo in self.photos:
            self.album1.contain_photo.add(photo)

    def test_album_size(self):
        """Test photos in album."""
        self.assertEquals(self.album1.contain_photo.count(), 50)

    def test_owner_match(self):
        """Test owner is correct."""
        for photo in self.photos:
            self.assertEquals(photo.user, self.album1.album_owner)

    def test_photos_in_multiple_albums(self):
        """Test photos are in multiple albums."""
        for photo in self.photos:
            self.album2.contain_photo.add(photo)
        for photo in self.photos:
            self.assertIn(photo, self.album1.contain_photo.all())
            self.assertIn(photo, self.album2.contain_photo.all())
