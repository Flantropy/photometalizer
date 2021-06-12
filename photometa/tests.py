from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, SimpleTestCase
from exif import Image as EXIFImage, WhiteBalance
from .models import Image
from .forms import ExifEditorForm
from exif import _app1_create


class TestExif(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test')
        self.obj = Image.objects.create(owner=self.user)
        self.obj.img = SimpleUploadedFile(
            name='test_image.jpg',
            content=open(r'C:\Users\User\PycharmProjects\pmdm\media\profile_pics\moto.jpg', 'rb').read(),
            content_type='image/jpeg')
        self.image = EXIFImage(self.obj.img.read())

    def test_has_exif(self):
        # l = self.image.list_all()
        # for v in l:
        #     print(type(self.image.get(v)), v, self.image.get(v))
        self.assertTrue(self.image.has_exif)

    def test_clear_exif(self):
        self.image.delete_all()
        self.assertEqual(self.image.list_all(), list())

    def test_setting_str_attr(self):
        self.image.make = 'python'
        self.assertEqual(self.image.make, 'python')

    def test_exception_on_missing_attr_type(self):
        with self.assertRaises(TypeError):
            self.image.make = 123

    def test_modify_special_tag(self):
        # setting attribute by Enum.member.value associated with it
        self.image.white_balance = 1
        self.assertEqual(self.image.white_balance, WhiteBalance.MANUAL)

    def test_adding_tags_to_cleaned_image(self):
        # safe clean
        [self.image.delete(atr) for atr in self.image.list_all()]
        self.image.make = 'python'
        self.assertEqual(self.image.make, 'python')
