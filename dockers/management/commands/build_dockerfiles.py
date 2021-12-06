import logging

from django.core.management import BaseCommand

from dockers.exceptions import brief_except, DockerfileIsNotExist
from dockers.module.docker_service import try_build_dockerfile
from dockers.module.docker_utils import get_dockers_json


class Command(BaseCommand):
    help = 'Build Dockerfiles'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for docker_json in get_dockers_json():
            try:
                try_build_dockerfile(docker_json)

            except DockerfileIsNotExist as e:
                logging.error(e)
                continue

            except Exception as e:
                logging.critical(brief_except())
