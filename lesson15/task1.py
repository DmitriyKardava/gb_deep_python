"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
* Для дочерних объектов указывайте родительскую директорию.
* Для каждого объекта укажите файл это или директория.
* Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
с учётом всех вложенных файлов и директорий.
"""
import argparse
import csv
import json
import os.path
import pickle
from pathlib import Path
import log


def dir2dict(work_dir: Path) -> dict:
    result = {}
    if not os.path.isdir(work_dir):
        log.logger.error(f"directory not exist {work_dir}")
        return result
    all_files = Path(work_dir).glob('**/*')
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


def save_file(func_name, file, data):
    return func_name(file, data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Сохранение содержимого директории в файл.")
    parser.add_argument('dir_name', type=str, help='Директория для сохранения')
    parser.add_argument("-o", "--out", dest="file_name", type=str, required=True,
                        help="Имя файла для сохранения")
    parser.add_argument("-f", "--format", dest="file_format", type=str, default="json",
                        help="Формат файла для сохранения json, csv, pickle")
    args = parser.parse_args()
    log.logger.info(f"Start parsing directory {args.dir_name}")
    file_name = args.file_name
    w_dir = dir2dict(args.dir_name)
    func = False
    if args.file_format == 'json':
        file_name = Path(args.file_name + '.json')
        func = dict2json
    elif args.file_format == 'csv':
        file_name = Path(args.file_name + '.csv')
        func = dict2csv
    elif args.file_format == 'pickle':
        file_name = Path(args.file_name + '.pickle')
        func = dict2pickle
    else:
        log.logger.error(f"Неизвестный формат файла {args.file_format}")
    if func:
        try:
            log.logger.info(f"Запись в файл {args.file_name}")
            save_file(func, file_name, w_dir)
        except Exception as err:
            log.logging.exception(err)
