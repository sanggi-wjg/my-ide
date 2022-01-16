from django.core.management import BaseCommand

from common.decorators import catch_error
from dockers.exceptions import DockerfileIsNotExist
from dockers.module.docker_service import build_dockerfile
from dockers.module.docker_utils import get_dockers_json


class Command(BaseCommand):
    help = 'Build Dockerfiles'

    def add_arguments(self, parser):
        pass

    @catch_error((DockerfileIsNotExist, Exception))
    def handle(self, *args, **options):
        for docker_json in get_dockers_json():
            build_dockerfile(docker_json)
