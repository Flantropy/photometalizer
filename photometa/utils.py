import exif
from exif import Image as EXIFImage


def get_exif(image):
    photo = EXIFImage(image.img.read())
    exif = photo.get_all()
    return exif


def get_all_exif_tags():
    return [tag for tag in list(exif._constants.ATTRIBUTE_ID_MAP.keys())[:-3]]


def safe_clear(image):
    [image.delete(attr) for attr in image.list_all()]


if __name__ == '__main__':
    pass
