from pathlib import Path
import cv2


def generate_video_thumbnail(media, output_folder="cache/thumbnails"):
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    try:
        video = cv2.VideoCapture(media.path)

        success, frame = video.read()

        if not success:
            return None

        thumbnail_name = f"{Path(media.name).stem}_thumb.jpg"
        thumbnail_path = Path(output_folder) / thumbnail_name

        cv2.imwrite(str(thumbnail_path), frame)

        video.release()

        return str(thumbnail_path)

    except Exception as e:
        print(f"Video thumbnail error for {media.name}: {e}")
        return None