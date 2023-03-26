import pathlib


def group_rename(new_ext: str, num_count: int, name_range=(), new_name='', old_ext='*', in_path='.'):
    in_files = pathlib.Path(in_path).glob(f"*.{old_ext}")
    count = 0
    for file in in_files:
        if file.is_file():
            count += 1
            new_name = f"{file.stem[name_range[0]:name_range[1]]}{new_name}{str(count).zfill(num_count)}.{new_ext}"
            new_name = pathlib.Path(in_path, new_name)
            file.replace(new_name)
            new_name = ''


if __name__ == "__main__":
    group_rename(in_path='../test', old_ext='txt', new_ext='qwe', num_count=3, name_range=(0, 3))
