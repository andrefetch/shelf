from pathlib import Path
from shelf.models import Note
import json

DEFAULT_PATH = Path.home() / ".shelf_data.json"

def load(path: Path = DEFAULT_PATH) -> list[Note]:
    if not path.exists():
        return []

    with open(path) as file:
        data = json.load(file)
    return [Note(**item) for item in data]

def save(notes: list[Note], path: Path = DEFAULT_PATH) -> None:
    
    with open(path, 'w') as file:
        json.dump([vars(n) for n in notes], file, indent=2)
