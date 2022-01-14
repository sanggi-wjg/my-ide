from django.db import models
from django.db.models import QuerySet

from dockers.models import DockerImage
from dockers.module.docker_vo import DockerJson


class DockerImageQuerySet(models.QuerySet):

    def get_image_build_success(self, docker_json: DockerJson) -> QuerySet['DockerImage']:
        try:
            self.get(
                image_name = docker_json.image_name,
                image_tag = docker_json.image_tag
            )
            image = self.filter(
                image_name = docker_json.image_name,
                image_tag = docker_json.image_tag
            )
        except DockerImage.DoesNotExist as e:
            raise Exception(f"{docker_json.image_name}-{docker_json.image_tag} is not exist")

        try:
            image = image.get(build_image_success = True)
        except DockerImage.DoesNotExist as e:
            raise Exception(f"{docker_json.image_name}-{docker_json.image_tag} is not build success")

        return image

    def publish(self, docker_json: DockerJson) -> QuerySet['DockerImage']:
        try:
            image = self.get(
                image_name = docker_json.image_name,
                image_tag = docker_json.image_tag
            )
        except DockerImage.DoesNotExist:
            image = self.create(
                image_name = docker_json.image_name,
                image_tag = docker_json.image_tag,
                local_port = docker_json.local_port
            )
        return image

    def update_build_image_success(self, image_id: int, result: str):
        rows = self.filter(
            id = image_id
        ).update(
            build_image_result = result,
            build_image_success = True
        )
        return rows

    def update_build_image_failed(self, image_id: int):
        rows = self.filter(
            id = image_id
        ).update(
            build_image_result = None,
            build_image_success = False
        )
        return rows

    def update_container_running_success(self, image_id: int):
        rows = self.filter(
            id = image_id
        ).update(
            container_is_running = True
        )
        return rows

    def update_container_running_failed(self, image_id: int):
        rows = self.filter(
            id = image_id
        ).update(
            container_is_running = False
        )
        return rows
