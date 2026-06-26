def sort_by_name(media_list):
    return sorted(media_list, key=lambda x: x.name.lower())


def sort_by_size(media_list, reverse=False):
    return sorted(media_list, key=lambda x: x.size, reverse=reverse)


def sort_by_type(media_list):
    return sorted(media_list, key=lambda x: x.media_type)