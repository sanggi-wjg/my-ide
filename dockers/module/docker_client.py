import docker
from docker.models.images import Image

from dockers.exceptions import DockerImageIsNotExist, DockerImageDuplicateExist
from dockers.module.docker_vo import DockerfileInfo


class MyDockerClient:
    base_url = 'unix://var/run/docker_www.sock'

    def __init__(self, base_url = None):
        # self.client = APIClient(base_url = self.base_url)
        if base_url:
            self.base_url = base_url
        self.client = docker.DockerClient(base_url = self.base_url)

    def build_dockerfile(self, dockerfile: DockerfileInfo) -> list:
        return [line.decode('utf-8') for line in self.client.images.build(
            path = dockerfile.dirpath, dockerfile = dockerfile.filepath,
            rm = True, tag = f"{dockerfile.image_name}-{dockerfile.image_tag}"
        )]

    def is_exist_docker_image_by_name(self, name: str):
        try:
            image = self.client.images.get(name)
        except docker.errors.ImageNotFound:
            # If the image does not exist.
            raise DockerImageIsNotExist(f"{name} image is not exist")
        except docker.errors.APIError as e:
            # If the server returns an error.
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
            raise DockerImageIsNotExist(f"{name} image is not exist")
        if len(images) > 1:
            raise DockerImageDuplicateExist(f"{name} image duplicated")

        return images.pop()

    def create_container_and_run(self, name: str, port: list):
        try:
            container = self.client.api.create_container(
                image = name, detach = True, name = name,
                ports = port,
                host_config = self.client.api.create_host_config(port_bindings = {
                    port: ('127.0.0.1', port)
                })
            )
        except docker.errors.ImageNotFound as e:
            # If the specified image does not exist.
            raise DockerImageIsNotExist(f"{name} image is not exist")
        except docker.errors.APIError as e:
            # If the server returns an error.
            raise e

        try:
            self.client.api.start(container.get("Id"))
        except (docker.errors.APIError, docker.errors.DeprecatedMethod) as e:
            # If the server returns an error.
            # If any argument besides ``container`` are provided.
            raise e
