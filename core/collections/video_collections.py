def get_video_collection(media):
    path = media.path.lower()

    if "screenrecord" in path or "screen recording" in path or "screen_record" in path:
        return "Screen Recordings"

    if "camera" in path or "dcim" in path:
        return "Camera Videos"

    if "whatsapp" in path:
        return "WhatsApp Videos"

    if "download" in path or "downloads" in path:
        return "Downloads"

    return "Other Videos"


def group_videos(media_list):
    collections = {}

    for media in media_list:
        if media.media_type != "video":
            continue

        collection_name = get_video_collection(media)

        if collection_name not in collections:
            collections[collection_name] = []

        collections[collection_name].append(media)

    return collections