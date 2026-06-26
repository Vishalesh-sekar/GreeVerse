def get_image_collection(media):
    path = media.path.lower()
    name = media.name.lower()

    if "camera" in path or "dcim" in path:
        return "Camera"

    if "screenshots" in path or "screenshot" in path:
        return "Screenshots"

    if "whatsapp" in path:
        return "WhatsApp Images"

    if "download" in path or "downloads" in path:
        return "Downloads"

    if "instagram" in path:
        return "Instagram"

    if name.endswith(".gif"):
        return "GIFs"

    return "Other Images"


def group_images(media_list):
    collections = {}

    for media in media_list:

        if media.media_type != "photo":
            continue

        collection = get_image_collection(media)
        if collection not in collections:
            collections[collection] = []
            collections[collection].append(media)
    
    return collections