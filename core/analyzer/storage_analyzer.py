def analyze_storage(media_list):

    stats = {
        "photo_size": 0,
        "video_size": 0,
        "audio_size": 0,
        "document_size": 0,
        "total_size": 0
    }

    for m in media_list:

        stats["total_size"] += m.size

        if m.media_type == "photo":
            stats["photo_size"] += m.size

        elif m.media_type == "video":
            stats["video_size"] += m.size

        elif m.media_type == "audio":
            stats["audio_size"] += m.size

        elif m.media_type == "document":
            stats["document_size"] += m.size

    return stats