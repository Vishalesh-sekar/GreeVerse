import hashlib
import json
from pathlib import Path


PASSWORD_FILE = Path("data/password.json")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def setup_password(password):
    PASSWORD_FILE.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "password_hash": hash_password(password)
    }

    with open(PASSWORD_FILE, "w") as file:
        json.dump(data, file, indent=4)

    return True


def password_exists():
    return PASSWORD_FILE.exists()


def verify_password(password):
    if not PASSWORD_FILE.exists():
        return False

    with open(PASSWORD_FILE, "r") as file:
        data = json.load(file)

    return data["password_hash"] == hash_password(password)