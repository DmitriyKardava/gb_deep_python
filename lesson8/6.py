import pickle
import csv
from pathlib import Path


def pickle2csv(in_file: Path, out_file: Path):
    with open(in_file, 'rb') as f:
        temp = pickle.load(f)

    with open(out_file, 'w') as f:
        fieldnames = temp[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(temp)


if __name__ == "__main__":
    pickle2csv(Path('../test.pickle'), Path('../test.csv'))
