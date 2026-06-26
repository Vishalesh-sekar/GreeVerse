from core.thumbnails.image_thumbnail import generate_image_thumbnail
from core.thumbnails.video_thumbnail import generate_video_thumbnail


def generate_thumbnail(media):
    if media.media_type == "photo":
        return generate_image_thumbnail(media)

    elif media.media_type == "video":
        return generate_video_thumbnail(media)

    return None