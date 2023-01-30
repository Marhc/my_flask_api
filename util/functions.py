import os


def filename(file_path):
    filename = os.path.basename(file_path)
    return os.path.splitext(filename)[0]
