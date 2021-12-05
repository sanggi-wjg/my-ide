import logging

from django.core.management import BaseCommand

from dockers.exceptions import brief_except, DockerfileIsNotExist
from dockers.models import DockerImage
from dockers.module.docker_client import MyDockerClient
from dockers.module.dockerfile_info import DockerfileInfo
from dockers.utils import get_dockerfile_path, get_dockers


class Command(BaseCommand):
    help = 'Build Dockerfiles'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for item in get_dockers():
            try:
                self.try_build_dockerfile(item)

            except DockerfileIsNotExist as e:
                logging.error(e)
                continue

            except Exception as e:
                logging.error(brief_except())

    def try_build_dockerfile(self, data: dict):
        # get dockerfile info
        image = DockerImage.objects.publish(data['image_name'], data['image_tag'])
        dirpath, filepath = get_dockerfile_path(f"{image.image_name}-{image.image_tag}")
        dockerfile_info = DockerfileInfo(dirpath, filepath, image.image_name, image.image_tag)
        logging.info(f"Try build Dockerfile : {dockerfile_info}")

        # build dockerfile
        client = MyDockerClient()
        result = client.build_dockerfile(dockerfile_info)

        # Check success or fail, then update.
        is_success = client.is_exist_docker_image_by_name(f"{image.image_name}-{image.image_tag}")
        DockerImage.objects.update_build_image_result(image.id, ''.join(result), is_success)
