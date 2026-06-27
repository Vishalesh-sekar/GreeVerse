from core.media_manager.media_manager import (
    rename_file,
    copy_file,
    move_file,
    safe_delete_file
)

from core.favorites.favorites_manager import (
    add_favorite,
    remove_favorite,
    is_favorite
)

from core.privacy.private_access import (
    mark_as_private,
    remove_from_private,
    is_private
)

from utils.file_utils import format_size


def rename_media(media, new_name):
    return rename_file(media, new_name)


def copy_media(media, destination_folder):
    return copy_file(media, destination_folder)


def move_media(media, destination_folder):
    return move_file(media, destination_folder)


def delete_media_to_trash(media):
    return safe_delete_file(media)


def toggle_favorite(media):
    if is_favorite(media):
        remove_favorite(media)
        return False

    add_favorite(media)
    return True


def toggle_private(media):
    if is_private(media):
        remove_from_private(media)
        return False

    mark_as_private(media)
    return True


def get_media_details(media):
    return (
        f"Name: {media.name}\n"
        f"Type: {media.media_type}\n"
        f"Extension: {media.extension}\n"
        f"Size: {format_size(media.size)}\n"
        f"Path: {media.path}"
    )