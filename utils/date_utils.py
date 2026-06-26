from datetime import datetime

def format_date(timestamp):

    return datetime.fromtimestamp(
        timestamp
    ).strftime("%d-%m-%Y %H:%M")

