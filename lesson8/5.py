import os.path
from pathlib import Path
import json
import pickle


def json2pickle(directory: Path):
    json_files = Path(directory).glob("*.json")
    for json_file in json_files:
        with open(json_file) as f:
            temp = json.load(f)
        pickle_file = Path(os.path.splitext(json_file)[0] + '.pickle')
        with open(pickle_file, 'wb') as f:
            pickle.dump(temp, f)


if __name__ == "__main__":
    json2pickle(Path(".."))
