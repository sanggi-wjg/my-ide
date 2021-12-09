from django.core.management import BaseCommand

from dockers.decorators import catch_error
from dockers.exceptions import DockerfileIsNotExist
from dockers.models import DockerImage
from dockers.module.docker_service import run_docker_image
from dockers.module.docker_utils import get_dockers_json


class Command(BaseCommand):
    help = 'Run docker image'

    def add_arguments(self, parser):
        pass

    @catch_error((DockerfileIsNotExist, Exception))
    def handle(self, *args, **options):
        for docker_json in get_dockers_json():
            image = DockerImage.objects.get_image_build_success(docker_json)
            run_docker_image(image)
