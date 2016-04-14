# from __future__ import unicode_literals
# from django.test import TestCase
# from .models import Photo, Album
# from django.db.models import ImageField
# from django.db.models.fields.files import ImageFieldFile
# from django.contrib.auth.models import User
# import factory


# class PhotoFactory(factory.django.DjangoModelFactory):
#     """Create Photo model for test."""

#     class Meta:
#         """Assign Photo model as product of factory."""

#         model = Photo


# class AlbumFactory(factory.django.DjangoModelFactory):
#     """Create Album model for test."""

#     class Meta:
#         """Assign Album model as product of factory."""

#         model = Album


# class TestPhoto(TestCase):
#     """Test Albums and Images and their relationships."""
#     def setUp(self):
#         self.test_user_1 = User.objects.create_user('testuser',
#                                                     'test@email.com',
#                                                     'testpassword')
#         self.test_album_1 = AlbumFactory.create(album_title='album 1', owner=self.test_user_1)
#         # self.album2 = Album(title='album 2', owner=self.test_user1)
#         self.test_photo_1 = PhotoFactory.create(title='photo 1', owner=self.test_user_1)
#         # self.image2 = PhotoFactory.create(title='image 2',
#         #                                   owner=self.test_user1)
#         self.test_album_1.save()
#         self.test_photo_1.save()
#         self.test_photo_1.albums.add(self.test_album_1)

#     def test_album_exists(self):
#         """Test album has been created."""
#         self.assertIsInstance(self.test_album_1, Album)

#     # def test_image_exists(self):
#     #     """Test image has been created."""
#     #     self.assertIsInstance(self.image1, Image)

#     # def test_album_title(self):
#     #     """Test album has title."""
#     #     self.assertEquals(self.album1.title, 'album 1')

#     # def test_image_title(self):
#     #     """Test image has title."""
#     #     self.assertEquals(self.image1.title, 'image 1')

#     # def test_album_default_description(self):
#     #     """Test album default description is empty string."""
#     #     self.assertEquals(self.album1.description, '')

#     # def test_image_default_description(self):
#     #     """Test image default description is empty string."""
#     #     self.assertEquals(self.image1.description, '')

#     # def test_album_date_uploaded(self):
#     #     """Test to verify date for date uploaded on album."""
#     #     self.assertIsInstance(self.album1.date_uploaded, datetime)

#     # def test_image_date_uploaded(self):
#     #     """Test to verify date for date uploaded on image."""
#     #     self.assertIsInstance(self.image1.date_uploaded, datetime)

#     # def test_album_date_modified(self):
#     #     """Test to verify the date changes upon modification."""
#     #     initial = self.image1.date_modified
#     #     self.assertEquals(initial, self.image1.date_modified)
#     #     self.image1.title = 'new title'
#     #     self.image1.save()
#     #     self.assertNotEqual(initial, self.image1.date_modified)

#     # def test_image_in_album(self):
#     #     """Test to verify that image can be in album."""
#     #     self.assertEquals(self.album1.images.all()[0], self.image1)

#     # def test_images_have_owner(self):
#     #     """Test to verify that images have owners."""
#     #     self.assertEquals(self.image1.owner, self.test_user1)

#     # def test_albums_have_owner(self):
#     #     """Test to verify that albums have owners."""
#     #     self.assertEquals(self.album1.owner, self.test_user1)

#     # def test_user_has_albums(self):
#     #     """Test to verify that user has albums."""
#     #     self.assertEquals(self.test_user1.albums.all().count(), 2)

#     # def test_user_has_images(self):
#     #     """Test to verify that user has images."""
#     #     self.assertEquals(self.test_user1.images.all().count(), 2)

#     # def test_image_has_image(self):
#     #     """Test to verify image has been created with an image."""
#     #     self.assertIsInstance(self.image1.photo, ImageFieldFile)
