from core.collections.image_collections import group_images
from core.collections.video_collections import group_videos
from core.collections.audio_collections import group_audio
from core.collections.document_collections import group_documents


def group_all_collections(media_list):
    return {
        "images": group_images(media_list),
        "videos": group_videos(media_list),
        "audio": group_audio(media_list),
        "documents": group_documents(media_list)
    }

def print_collections(collections):
    for section, groups in collections.items():
        print(f"\n===== {section.upper()} COLLECTIONS =====")

        if not groups:
            print("No files found")
            continue

        for collection_name, items in groups.items():
            print(f"{collection_name}: {len(items)} file(s)")