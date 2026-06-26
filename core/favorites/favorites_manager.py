import json
from pathlib import Path

FAVORITES_FILE = Path("data/favorites.json")


def load_favorites():
    if not FAVORITES_FILE.exists():
        return []

    with open(FAVORITES_FILE, "r") as file:
        data = json.load(file)

    return data.get("favorites", [])


def save_favorites(favorites):
    FAVORITES_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(FAVORITES_FILE, "w") as file:
        json.dump({"favorites": favorites}, file, indent=4)


def add_favorite(media):
    favorites = load_favorites()

    if media.path not in favorites:
        favorites.append(media.path)
        save_favorites(favorites)

    return True


def remove_favorite(media):
    favorites = load_favorites()

    if media.path in favorites:
        favorites.remove(media.path)
        save_favorites(favorites)

    return True


def is_favorite(media):
    return media.path in load_favorites()


def get_favorite_media(media_list):
    favorites = load_favorites()

    return [media for media in media_list if media.path in favorites]