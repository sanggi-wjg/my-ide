import logging

from django.core.management import BaseCommand

from dockers.exceptions import brief_except, DockerfileIsNotExist
from dockers.models import DockerImage
from dockers.module.docker_service import try_run_docker_image
from dockers.module.docker_utils import get_dockers_json


class Command(BaseCommand):
    help = 'Run docker image'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for docker_json in get_dockers_json():
            try:
                image = DockerImage.objects.get_image_build_success(docker_json)
                try_run_docker_image(image)

            except DockerfileIsNotExist as e:
                logging.error(e)
                continue

            except Exception as e:
                logging.critical(brief_except())
