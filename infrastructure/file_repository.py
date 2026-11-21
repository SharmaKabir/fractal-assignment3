import json
from pathlib import Path


class FileRepository:
    """Infrastructure implementation for persisting request dictionaries as JSON."""

    def __init__(self, file_path="data/requests.json"):
        self.file_path = Path(file_path)

    def load(self):
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                content = file.read().strip()
                if not content:
                    return []
                data = json.loads(content)
        except json.JSONDecodeError as error:
            raise ValueError("The requests JSON file is invalid") from error

        if not isinstance(data, list):
            raise ValueError("The requests JSON file must contain a JSON list")
        return data

    def save(self, requests):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(requests, file, indent=4)
            file.write("\n")
