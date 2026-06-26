from pathlib import Path
from models.media import Media

VIDEO_EXTENSIONS = {
    ".mp4", ".mkv", ".avi", ".mov", ".webm", "3gp"
}

def scan_videos(folder_path):
    videos = []

    for file in Path(folder_path).rglob("*"):
        if file.is_file() and file.suffix.lower() in VIDEO_EXTENSIONS:

            media = Media(
                name = file.name,
                path = str(file),
                media_type = "video",
                extension = file.suffix.lower(),
                size = file.stat().st_size,
                created_date=file.stat().st_ctime
            )
            videos.append(media)

    return videos