from django.db import models
from django.db.models import QuerySet

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


class DockerImage(models.Model):
    objects = DockerImageQuerySet.as_manager()

    BUILD_SUCCESS = True
    BUILD_FAILED = False
    BUILD_IMAGE_SUCCESS_CHOICES = [(BUILD_SUCCESS, 'Success'), (BUILD_FAILED, 'Failed')]

    id = models.BigAutoField(primary_key = True)
    image_name = models.CharField(max_length = 100)
    image_tag = models.CharField(max_length = 100)
    local_port = models.IntegerField(default = 0)

    build_image_result = models.TextField(null = True, default = None)
    build_image_success = models.IntegerField(null = False, default = BUILD_FAILED, choices = BUILD_IMAGE_SUCCESS_CHOICES)

    container_is_running = models.IntegerField(null = False, default = BUILD_FAILED, choices = BUILD_IMAGE_SUCCESS_CHOICES)

    class Meta:
        db_table = 'dockers'
        ordering = ['id', ]
        unique_together = (('image_name', 'image_tag'),)

    def __str__(self):
        return f"<DockerImage object {self.id}> {self.image_name} - {self.image_tag} build: {self.build_image_success} running: {self.container_is_running}"
