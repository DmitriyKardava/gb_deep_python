import pathlib


def sort_by_type(dir_to_sort: pathlib.Path):
    types = [
        {'type_name': 'video',
         'path': 'video',
         'extensions': ['*.avi', '*.mp4', '*.mkv'],
         },
        {'type_name': 'images',
         'path': 'img',
         'extensions': ['*.jpg', '*.jpeg', '*.bmp', '*.tiff', '*.gif'],
         },
        {'type_name': 'documents',
         'path': 'doc',
         'extensions': ['*.txt', '*.doc', '*.docx', '*.xls', '*.xlsx'],
         },

    ]
    for file_type in types:
        pathlib.Path(dir_to_sort, file_type['path']).mkdir(parents=True, exist_ok=True)
        for ext in file_type['extensions']:
            files = pathlib.Path(dir_to_sort).glob(ext)
            for file in files:
                file.replace(pathlib.Path(dir_to_sort, file_type['path'], file.name))
    return True


if __name__ == "__main__":
    sort_by_type(pathlib.Path('../test'))
