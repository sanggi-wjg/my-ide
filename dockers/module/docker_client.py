import logging
from typing import Tuple, Iterable, Any

import docker
from docker.models.images import Image

from common.exceptions import brief_except
from dockers.exceptions import DockerImageIsNotExist, DockerImageDuplicateExist
from dockers.models import DockerImage
from dockers.module.docker_vo import DockerfileInfo


class MyDockerClient:
    base_url = 'unix://var/run/docker_www.sock'

    def __init__(self, base_url = None):
        # self.client = APIClient(base_url = self.base_url)
        if base_url:
            self.base_url = base_url
        self.client = docker.DockerClient(base_url = self.base_url)

    def build_dockerfile(self, dockerfile: DockerfileInfo) -> Tuple[Image, str]:
        logging.info(f"Build dockerfile : {dockerfile}")

        result: Tuple[Image, Iterable] = self.client.images.build(
            path = dockerfile.dirpath, dockerfile = dockerfile.filepath,
            rm = True, tag = f"{dockerfile.image_name}-{dockerfile.image_tag}"
        )
        return result[0], ''.join([r.get('stream', '') for r in result[1]])

    def is_exist_docker_image_by_name(self, name: str):
        try:
            image = self.client.images.get(name)
        except docker.errors.ImageNotFound:
            # If the image does not exist.
            logging.error(f"{name} image is not exist")
            raise DockerImageIsNotExist(f"{name} image is not exist")
        except docker.errors.APIError as e:
            # If the server returns an error.
            logging.critical(brief_except())
            raise e

        if image.tags.pop().replace(":latest", '') == name:
            return True

        return False

    def get_docker_images(self, name = None):
        try:
            return self.client.images.list(name)
        except docker.errors.APIError as e:
            # If the server returns an error.
            raise e

    def get_docker_image_by_name(self, name: str) -> Image:
        images = self.get_docker_images(name)
        if len(images) == 0:
            logging.error(f"{name} image is not exist")
            raise DockerImageIsNotExist(f"{name} image is not exist")
        if len(images) > 1:
            logging.error(f"{name} image duplicated")
            raise DockerImageDuplicateExist(f"{name} image duplicated")

        return images.pop()

    def get_create_host_config(self, port: int) -> dict:
        return self.client.api.create_host_config(port_bindings = {
            port: ('127.0.0.1', port)
        })

    def create_container_and_run(self, image: DockerImage):
        name = f"{image.image_name}-{image.image_tag}"
        try:
            logging.info(f"Docker run image : {name}")

            if image.local_port:
                container = self.client.api.create_container(
                    image = name, detach = True, name = name, ports = [image.local_port],
                    host_config = self.get_create_host_config(image.local_port)
                )
            else:
                container = self.client.api.create_container(image = name, detach = True, name = name)

        except docker.errors.ImageNotFound as e:
            # If the specified image does not exist.
            logging.error(f"{name} image is not exist")
            raise DockerImageIsNotExist(f"{name} image is not exist")
        except docker.errors.APIError as e:
            # If the server returns an error.
            logging.critical(brief_except())
            raise e

        try:
            self.client.api.start(container.get("Id"))
        except (docker.errors.APIError, docker.errors.DeprecatedMethod) as e:
            # If the server returns an error.
            # If any argument besides ``container`` are provided.
            logging.critical(brief_except())
            raise e

        return True

    def exec_run_container(self, name: str, cmd: str):
        # conn = self.get_docker_image_by_name(name)
        container = self.client.containers.list(filters = { 'name': name }).pop()
        container = self.client.containers.get(container.id)
        result: Tuple[int, Any] = container.exec_run(cmd)
        return eval(result[1].decode('utf-8'))
