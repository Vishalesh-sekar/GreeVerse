def get_document_collection(media):
    extension = media.extension.lower()

    if extension == ".pdf":
        return "PDF Files"

    if extension in [".doc", ".docx"]:
        return "Word Documents"

    if extension in [".xls", ".xlsx", ".csv"]:
        return "Excel Files"

    if extension in [".ppt", ".pptx"]:
        return "PowerPoint Files"

    if extension in [".txt", ".md"]:
        return "Text Files"

    if extension in [".zip", ".rar", ".7z"]:
        return "Archives"

    return "Other Documents"


def group_documents(media_list):
    collections = {}

    for media in media_list:
        if media.media_type != "document":
            continue

        collection_name = get_document_collection(media)

        if collection_name not in collections:
            collections[collection_name] = []

        collections[collection_name].append(media)

    return collections