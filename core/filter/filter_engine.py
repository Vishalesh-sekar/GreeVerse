def filter_by_type(media_list, media_type):
    return [m for m in media_list if m.media_type == media_type]


def filter_by_extension(media_list, extension):
    return [m for m in media_list if m.extension == extension]


def filter_large_files(media_list, min_size):
    return [m for m in media_list if m.size >= min_size]