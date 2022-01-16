import os
import random
import string
from typing import Generator, List

from dockers.models import DockerImage


def validate_dir(dirpath: str):
    """

    :param dirpath:
    :type dirpath:
    :return:
    :rtype:
    """
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)


def get_directories(images: List['DockerImage'], dirpath_root: str) -> dict:
    """

    :param images:
    :type images:
    :param dirpath_root:
    :type dirpath_root:
    :return:
    :rtype:
    """
    directories = { }

    for image in images:
        sub_dir = image.sub_folder_name
        dirpath = os.path.join(dirpath_root, sub_dir)
        directories.setdefault(sub_dir, [])

        for root, dirs, files in os.walk(dirpath):
            for d in dirs:
                directories[sub_dir].append(d)

    return directories


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
