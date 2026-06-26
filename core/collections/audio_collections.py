def get_audio_collection(media):
    path = media.path.lower()
    name = media.name.lower()

    if "recording" in path or "recordings" in path or "voice" in path:
        return "Recordings"

    if "whatsapp" in path:
        return "WhatsApp Audio"

    if "music" in path or "songs" in path:
        return "Music"

    if "download" in path or "downloads" in path:
        return "Downloads"

    if name.endswith(".m4a") or name.endswith(".aac"):
        return "Mobile Audio"

    return "Other Audio"


def group_audio(media_list):
    collections = {}

    for media in media_list:
        if media.media_type != "audio":
            continue

        collection_name = get_audio_collection(media)

        if collection_name not in collections:
            collections[collection_name] = []

        collections[collection_name].append(media)

    return collections