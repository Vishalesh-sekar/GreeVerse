from pathlib import Path
from PIL import Image


def generate_image_thumbnail(media, output_folder="cache/thumbnails", size=(200, 200)):
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    try:
        image = Image.open(media.path)
        image.thumbnail(size)

        thumbnail_name = f"{Path(media.name).stem}_thumb.jpg"
        thumbnail_path = Path(output_folder) / thumbnail_name

        image.convert("RGB").save(thumbnail_path, "JPEG")

        return str(thumbnail_path)

    except Exception as e:
        print(f"Thumbnail error for {media.name}: {e}")
        return None