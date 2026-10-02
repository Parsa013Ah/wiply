import json
from pathlib import Path

DATA_DIR = Path.home() / ".wiply"
DATA_FILE = DATA_DIR / "data.json"


def load_data():
    if not DATA_FILE.exists():
        return {"active": [], "history": []}
    try:
        with open(DATA_FILE) as f:
            data = json.load(f)
            if "active" not in data:
                data["active"] = []
            if "history" not in data:
                data["history"] = []
            return data
    except (json.JSONDecodeError, KeyError):
        return {"active": [], "history": []}


def save_data(data):
    DATA_DIR.mkdir(exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
