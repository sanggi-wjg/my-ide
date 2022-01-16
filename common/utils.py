import os
import random
import string
from typing import Generator


def get_directories(dirpath: str):
    filenames = []
    for root, dirs, files in os.walk(dirpath):
        print(root, dirs, files)
        if files:
            filenames.extend(files)
    return filenames


def validate_dir(dirpath: str):
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)


def get_dir_filenames(dirpath: str) -> Generator:
    """
    :param dirpath: directory 경로
    :return: 파일 이름들
    :rtype: Generator[str]
    """
    return (f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f)))


def read_file_lines(filepath: str) -> str:
    """
    :param filepath: 파일 경로
    :return: 파일 내용
    :rtype: str
    """
    lines = []
    with open(filepath, 'r') as file:
        for line in file.readlines():
            lines.append(line)
    return ''.join(lines)


def id_generator(size: int = 6, text: str = string.ascii_uppercase + string.digits) -> str:
    return ''.join(random.choice(text) for _ in range(size))
