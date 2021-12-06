import logging

from django.core.management import BaseCommand

from dockers.exceptions import brief_except, DockerfileIsNotExist
from dockers.module.docker_utils import get_dockers


class Command(BaseCommand):
    help = 'Run docker image'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for docker in get_dockers():
            try:
                pass
            except DockerfileIsNotExist as e:
                logging.error(e)
                continue

            except Exception as e:
                logging.critical(brief_except())
