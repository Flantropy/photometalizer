from exif import Image as EXIFImage


def format_exif(raw_exf: EXIFImage):
    exif = []
    for tag in raw_exf.list_all():
        exif.append({tag: raw_exf.get(str(tag))})
    return exif


def clear_meta(path):
    with open(path, 'rb') as image_file:
        image = EXIFImage(image_file)
    image.delete_all()
    with open(path, 'wb') as new_image_file:
        new_image_file.write(image.get_file())


if __name__ == '__main__':
    print('hello')
