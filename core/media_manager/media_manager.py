from pathlib import Path
import os
import shutil


def file_exists(media):
    return Path(media.path).exists()


def open_file(media):
    if not file_exists(media):
        return False

    os.startfile(media.path)  # Windows only
    return True


def rename_file(media, new_name):
    old_path = Path(media.path)

    if not old_path.exists():
        return None

    new_path = old_path.with_name(new_name)

    old_path.rename(new_path)

    media.name = new_path.name
    media.path = str(new_path)
    media.extension = new_path.suffix.lower()

    return media


def delete_file(media):
    path = Path(media.path)

    if not path.exists():
        return False

    path.unlink()
    return True


def copy_file(media, destination_folder):
    destination = Path(destination_folder)
    destination.mkdir(parents=True, exist_ok=True)

    new_path = destination / media.name

    shutil.copy2(media.path, new_path)

    return str(new_path)


def move_file(media, destination_folder):
    destination = Path(destination_folder)
    destination.mkdir(parents=True, exist_ok=True)

    old_path = Path(media.path)
    new_path = destination / media.name

    shutil.move(str(old_path), str(new_path))

    media.path = str(new_path)

    return media

def safe_delete_file(media, trash_folder="data/trash"):
    destination = Path(trash_folder)
    destination.mkdir(parents=True, exist_ok=True)

    old_path = Path(media.path)

    if not old_path.exists():
        return None

    new_path = destination / media.name

    counter = 1
    while new_path.exists():
        new_path = destination / f"{old_path.stem}_{counter}{old_path.suffix}"
        counter += 1

    shutil.move(str(old_path), str(new_path))

    media.path = str(new_path)

    return media