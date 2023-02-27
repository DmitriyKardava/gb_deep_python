import json
import csv
import pickle
from pathlib import Path


def dir2dict(work_dir: Path) -> dict:
    all_files = Path(work_dir).glob('**/*')
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


def dict2json(json_file: Path, data: dict):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def dict2csv(csv_file: Path, data: dict):
    with open(csv_file, 'w', encoding='utf-8') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(data)


def dict2pickle(pickle_file: Path, data: dict):
    with open(pickle_file, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    w_dir = dir2dict(Path('../'))
    dict2json(Path('../catalog.json'), w_dir)
    dict2csv(Path('../catalog.csv'), w_dir)
    dict2pickle(Path('../catalog.pickle'), w_dir)
