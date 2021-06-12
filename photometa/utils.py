import exif
from django.core.files.base import ContentFile
from exif import Image as EXIFImage

from photometa.models import Image


def get_exif(image):
    photo = EXIFImage(image.img.read())
    exif = photo.get_all()
    return exif


def safe_clear(image: EXIFImage):
    [image.delete(attr) for attr in image.get_all() if not attr.startswith('_')]


def write_image_with_new_meta(request, image: EXIFImage):
    new_file = image.get_file()
    new_obj = Image()
    new_obj.owner = request.user
    new_obj.img.save(name='new_image.jpg', content=ContentFile(new_file))
    new_obj.save()


if __name__ == '__main__':
    pass
