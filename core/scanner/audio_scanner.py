from pathlib import Path
from models.media import Media

AUDIO_EXTENSIONS = {
    ".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a"
}

def scan_audios(folder_path):
    audios = []

    for file in Path(folder_path).rglob("*"):
        if file.is_file() and file.suffix.lower() in AUDIO_EXTENSIONS:

            media = Media(
                name = file.name,
                path = str(file),
                media_type = "audio",
                extension = file.suffix.lower(),
                size = file.stat().st_size,
                created_date=file.stat().st_ctime
            )
            audios.append(media)

    return audios