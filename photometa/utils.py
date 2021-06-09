from exif import Image as EXIFImage


def retrieve_exif(path):
    with open(path, 'rb') as image_file:
        image = EXIFImage(image_file)

    exif = []
    for tag in image.list_all():
        exif.append({tag: image.get(str(tag))})
    return exif


def clear_meta(path):
    with open(path, 'rb') as image_file:
        image = EXIFImage(image_file)
    image.delete_all()
    with open(path, 'wb') as new_image_file:
        new_image_file.write(image.get_file())


if __name__ == '__main__':
    data = retrieve_exif(r'C:\Users\User\PycharmProjects\pmdm\media\profile_pics\Canon.jpg')
    print(data)
