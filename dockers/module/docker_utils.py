import os
from typing import Tuple, List

from dockers.exceptions import DockerfileIsNotExist
from dockers.module.docker_vo import Dockers
from my_ide.settings import DOCKERFILES_ROOT, DOCKERS


def get_dockers() -> List[Dockers]:
    return [
        Dockers(d['image_name'], d['image_tag'], d['local_port'])
        for d in DOCKERS
    ]


def get_dockerfile_path(dir_path: str) -> Tuple[str, str]:
    dockerfile_dir = os.path.join(DOCKERFILES_ROOT, dir_path)
    dockerfile_path = os.path.join(dockerfile_dir, "Dockerfile")

    if not os.path.exists(dockerfile_path):
        raise DockerfileIsNotExist(f"{dockerfile_path} is not exist")

    return dockerfile_dir, dockerfile_path
