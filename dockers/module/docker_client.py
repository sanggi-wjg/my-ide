import docker

from dockers.exceptions import DockerImageIsNotExist, DockerImageDuplicateExist
from dockers.module.dockerfile_info import DockerfileInfo


class MyDockerClient:
    base_url = 'unix://var/run/docker_www.sock'

    def __init__(self):
        # self.client = APIClient(base_url = self.base_url)
        self.client = docker.DockerClient(base_url = self.base_url)

    def build_dockerfile(self, dockerfile: DockerfileInfo) -> list:
        return [line.decode('utf-8') for line in self.client.images.build(
            path = dockerfile.dirpath, dockerfile = dockerfile.filepath,
            rm = True, tag = f"{dockerfile.image_name}-{dockerfile.image_tag}"
        )]

    def is_exist_docker_image_by_name(self, name: str):
        image = self.client.images.get(name)
        if image.tags.pop().replace(":latest", '') == name:
            return True

        return False

    def get_docker_images(self, name = None):
        return self.client.images.list(name)

    def get_docker_image_by_name(self, name: str):
        images = self.get_docker_images(name)
        if len(images) == 0:
            raise DockerImageIsNotExist(f"{name} image is not exist")
        if len(images) > 1:
            raise DockerImageDuplicateExist(f"{name} image duplicated")

        return images.pop()
