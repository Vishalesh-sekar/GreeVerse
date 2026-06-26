def search_media(media_list, query):
    query = query.lower().strip()

    if not query:
        return media_list
        
    results = []

    for media in media_list:

        # search by name
        if query in media.name.lower():
            results.append(media)
            continue

        # search by extension
        if query.startswith("."):
            if media.extension == query:
                results.append(media)
                continue

        # search by media type
        if query in media.media_type.lower():
            results.append(media)

    return results