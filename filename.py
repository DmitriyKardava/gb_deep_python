"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла
"""
from os.path import abspath


def path_split(full_path: str):
    name = full_path.split('/')[-1].split('.')[0]
    ext = full_path.split('.')[-1]
    path = full_path.removesuffix(full_path.split('/')[-1])
    return path, name, ext


print(path_split(abspath(__file__)))
