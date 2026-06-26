def calculate_statistics(media_list):

    stats = {
        "photos": 0,
        "videos": 0,
        "audio": 0,
        "documents": 0,
        "total_files": 0,
        "total_size": 0
    }

    for media in media_list:

        stats["total_files"] += 1
        stats["total_size"] += media.size

        if media.media_type == "photo":
            stats["photos"] += 1

        elif media.media_type == "video":
            stats["videos"] += 1

        elif media.media_type == "audio":
            stats["audio"] += 1

        elif media.media_type == "document":
            stats["documents"] += 1

    return stats