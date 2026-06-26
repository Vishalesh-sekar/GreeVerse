import json
from pathlib import Path


PRIVATE_FILE = Path("data/private_files.json")


def load_private_files():
    if not PRIVATE_FILE.exists():
        return []

    with open(PRIVATE_FILE, "r") as file:
        data = json.load(file)

    return data.get("private_files", [])


def save_private_files(private_files):
    PRIVATE_FILE.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "private_files": private_files
    }

    with open(PRIVATE_FILE, "w") as file:
        json.dump(data, file, indent=4)


def mark_as_private(media):
    private_files = load_private_files()

    if media.path not in private_files:
        private_files.append(media.path)
        save_private_files(private_files)

    return True


def remove_from_private(media):
    private_files = load_private_files()

    if media.path in private_files:
        private_files.remove(media.path)
        save_private_files(private_files)

    return True


def is_private(media):
    private_files = load_private_files()

    return media.path in private_files