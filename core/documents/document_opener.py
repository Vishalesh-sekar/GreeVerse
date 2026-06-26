from pathlib import Path
import os
import platform
import subprocess


def document_exists(media):
    return Path(media.path).exists()


def open_document(media):
    if media.media_type != "document":
        print("This is not a document")
        return False

    if not document_exists(media):
        print("Document not found")
        return False

    try:
        system_name = platform.system()

        if system_name == "Windows":
            os.startfile(media.path)

        elif system_name == "Darwin":
            subprocess.run(["open", media.path], check=True)

        else:
            subprocess.run(["xdg-open", media.path], check=True)

        return True

    except Exception as e:
        print(f"Unable to open document: {e}")
        return False