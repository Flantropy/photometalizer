import exif


def foo():
    for tag in list(exif._constants.ATTRIBUTE_ID_MAP.keys())[:-3]:
        print(type(tag))


def get_all_exif_tags():
    return [tag for tag in list(exif._constants.ATTRIBUTE_ID_MAP.keys())[:-3]]


if __name__ == '__main__':
    foo()
