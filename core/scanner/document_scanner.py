from pathlib import Path
from models.media import Media

DOCUMENT_EXTENSIONS = {
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"
}

def scan_documents(folder_path):
    documents = []

    for file in Path(folder_path).rglob("*"):
        if file.is_file() and file.suffix.lower() in DOCUMENT_EXTENSIONS:

            media = Media(
                name = file.name,
                path = str(file),
                media_type = "document",
                extension = file.suffix.lower(),
                size = file.stat().st_size,
                created_date=file.stat().st_ctime

            )
            documents.append(media)

    return documents