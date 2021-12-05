from docker import APIClient

from dockers.module.dockerfile_info import DockerfileInfo


class MyDockerClient:
    base_url = 'unix://var/run/docker_www.sock'

    def __init__(self):
        self.client = APIClient(base_url = self.base_url)

    def build_dockerfile(self, dockerfile: DockerfileInfo) -> list:
        return [line.decode('utf-8') for line in self.client.build(
            path = dockerfile.dirpath, dockerfile = dockerfile.filepath,
            rm = True, tag = f"{dockerfile.image_name}-{dockerfile.image_tag}"
        )]
