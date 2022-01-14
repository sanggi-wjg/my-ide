from django.db import models

from dockers.module.docker_vo import DockerJson
from dockers.querysets import DockerImageQuerySet


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
