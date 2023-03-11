import json
import csv
import pickle
from pathlib import Path


class DirTraversal:
    def __init__(self, work_dir: Path):
        self.work_dir = work_dir
        self.data = self._dir2dict()

    def _dir2dict(self) -> dict:
        all_files = Path(self.work_dir).glob('**/*')
        result = {}
        for file in all_files:
            if file.is_dir():
                f_type = 'directory'
                size = sum(file.stat(follow_symlinks=False).st_size for _ in file.rglob('*'))
            elif file.is_file():
                f_type = 'file'
                size = file.stat(follow_symlinks=False).st_size
            else:
                f_type = ''
                size = 0
            result[str(file)] = {"name": file.name, "f_type": f_type, "size": size, 'parent': str(file.parent)}
        return result

    def save_json(self, json_file: Path):
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def save_csv(self, csv_file: Path):
        with open(csv_file, 'w', encoding='utf-8') as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)
            wr.writerow(self.data)

    def save_pickle(self, pickle_file: Path):
        with open(pickle_file, 'wb') as f:
            pickle.dump(self.data, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    my_dir = DirTraversal(Path("./"))
    my_dir.save_pickle(Path("catalog.pickle"))
    my_dir.save_json(Path('catalog.json'))
    my_dir.save_csv(Path('catalog.csv'))
