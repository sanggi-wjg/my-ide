import os
from typing import Tuple, List

from common.utils import get_dir_filenames, read_file_lines
from dockers.exceptions import DockerfileIsNotExist
from dockers.module.docker_vo import DockerJson
from my_ide.settings import DOCKERFILES_ROOT, DOCKERS


def get_dockers_json() -> List[DockerJson]:
    """
    :return: settings 에 설정한 dockers.json 파일 읽어온 것에 대한 DockerJson Object
    :rtype: List[DockerJson]
    """
    return [
        DockerJson(d['image_name'], d['image_tag'], d['local_port'])
        for d in DOCKERS
    ]


def get_dockerfile_path(dir_path: str) -> Tuple[str, str]:
    """
    :param dir_path:
    :type dir_path:
    :return: 생성 되어 있는 Dockerfile 의 Directory 경로와 Dockerfile 경로
    :rtype: Tuple[str, str]
    """
    dockerfile_dir = os.path.join(DOCKERFILES_ROOT, dir_path)
    dockerfile_path = os.path.join(dockerfile_dir, "Dockerfile")

    if not os.path.exists(dockerfile_path):
        raise DockerfileIsNotExist(f"{dockerfile_path} is not exist")

    return dockerfile_dir, dockerfile_path


def read_dockerfiles_dir_files(dirpath: str) -> dict:
    """
    :param dirpath:
    :return: { 파일 이름 : 파일 내용 }
    :rtype: dict
    """
    result = { }
    for name in get_dir_filenames(dirpath):
        result.setdefault(name, read_file_lines(os.path.join(dirpath, name)))

    return result
