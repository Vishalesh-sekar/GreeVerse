from dataclasses import dataclass

@dataclass
class Media:
    name: str
    path: str
    media_type: str
    extension: str
    size: int
    created_date: float