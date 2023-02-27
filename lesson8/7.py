import csv
import pickle
from pathlib import Path


def csv2pickle_str(in_file: Path):
    with open(in_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            print(pickle.dumps(row))


if __name__ == "__main__":
    csv2pickle_str(Path('../test.csv'))

