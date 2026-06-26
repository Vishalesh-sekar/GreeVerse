from core.scanner.image_scanner import scan_images
from core.scanner.video_scanner import scan_videos
from core.scanner.audio_scanner import scan_audios
from core.scanner.document_scanner import scan_documents

def scan_all(folder):
    media = []

    media.extend(scan_images(folder))
    media.extend(scan_videos(folder))
    media.extend(scan_audios(folder))
    media.extend(scan_documents(folder))

    return media


