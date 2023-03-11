from math import sqrt
from random import randint
import json
import csv

PARM_COUNT = 1000
MIN_PARM = -1000
MAX_PARM = 1000


def gen_param_csv():
    with open('data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(PARM_COUNT):
            writer.writerow((randint(MIN_PARM, MAX_PARM),
                             randint(MIN_PARM, MAX_PARM),
                             randint(MIN_PARM, MAX_PARM)))


def read_csv_parm(func):
    def wrapper():
        with open('data.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                func(int(row[0]), int(row[1]), int(row[2]))
    return wrapper


def save_json_result(func):
    data = {}

    def wrapper(*args, **kwargs):
        data[str(args)] = func(*args, **kwargs)
        if len(data) == PARM_COUNT:
            print(data)
            with open('result.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
    return wrapper


@read_csv_parm
@save_json_result
def quadratic(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return False
    x1 = (-b + sqrt(d)) / 2 * a
    x2 = (-b - sqrt(d)) / 2 * a
    return x1, x2


if __name__ == "__main__":
    gen_param_csv()
    quadratic()
