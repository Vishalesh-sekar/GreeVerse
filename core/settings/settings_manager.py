import json
from pathlib import Path

SETTINGS_FILE = Path("data/settings.json")

DEFAULT_SETTINGS = {
    "theme": "light",
    "grid_size": 3,
    "sort_by": "name",
    "show_private_files": False
}


def load_settings():
    if not SETTINGS_FILE.exists():
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS

    with open(SETTINGS_FILE, "r") as file:
        return json.load(file)


def save_settings(settings):
    SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)


def update_setting(key, value):
    settings = load_settings()
    settings[key] = value
    save_settings(settings)

    return settings