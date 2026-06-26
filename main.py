from core.scanner.media_scanner import scan_all
from database.database import create_database
from utils.file_utils import format_size
from utils.date_utils import format_date
from core.statistics.media_statistics import calculate_statistics


all_media = scan_all("test_media")

stats = calculate_statistics(all_media)
print("\n===== GreeVerse Summary =====\n")

print(f"Photos      : {stats['photos']}")
print(f"Videos      : {stats['videos']}")
print(f"Audio       : {stats['audio']}")
print(f"Documents   : {stats['documents']}")

print()
print(f"Total Files : {stats['total_files']}")
print(f"Total Size  : {format_size(stats['total_size'])}")