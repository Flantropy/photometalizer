from django.test import TestCase, SimpleTestCase
from exif import Image
from .models import Image

class TestExif(SimpleTestCase):
    def setUp(self):
        with open('media/profile_pics/Canon.jpg', 'rb') as image_file:
            self.image = Image(image_file)

    def test_has_exif(self):
        self.assertTrue(self.image.has_exif)


class MyTest(TestCase):

    def setUp(self):
        self.myvar = 10

    def tearDown(self):
        pass

    def test_first(self):
        self.assertEqual(self.myvar, 10)

    def test_second(self):
        self.assertNotEqual(self.myvar, 11)
