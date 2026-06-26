def format_size(size):

    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:   
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} TB"

def get_file_extension(path):
    return path.split(".")[-1].lower()


def is_valid_media(extension, valid_set):
    return extension in valid_set