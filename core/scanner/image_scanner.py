from pathlib import Path
from models.media import Media

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"
}

def scan_images(folder_path):
    images = []

    for file in Path(folder_path).rglob("*"):
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS:

            media = Media(
                name = file.name,
                path = str(file),
                media_type = "photo",
                extension = file.suffix.lower(),
                size = file.stat().st_size,
                created_date=file.stat().st_ctime
            )
            images.append(media)

    return images