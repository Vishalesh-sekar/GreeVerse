from core.scanner.media_scanner import scan_all
from core.filter.filter_engine import filter_by_type

MEDIA_FOLDER = "test_media"

all_media = []


def load_media():
    global all_media
    all_media = scan_all(MEDIA_FOLDER)
    return all_media


def get_images():
    return filter_by_type(all_media, "photo")


def get_videos():
    return filter_by_type(all_media, "video")


def get_audio():
    return filter_by_type(all_media, "audio")


def get_documents():
    return filter_by_type(all_media, "document")