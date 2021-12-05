from django.db import models
from django.db.models import QuerySet


class DockerImageQuerySet(models.QuerySet):

    def publish(self, image_name: str, image_tag: str) -> QuerySet['DockerImage']:
        try:
            result = self.get(image_name = image_name, image_tag = image_tag)
        except DockerImage.DoesNotExist:
            result = self.create(image_name = image_name, image_tag = image_tag)
        return result

    def update_build_image_result(self, image_id: int, result: str, is_success: bool):
        rows = self.filter(
            id = image_id
        ).update(
            build_image_result = result,
            build_image_success = is_success
        )
        return rows


class DockerImage(models.Model):
    objects = DockerImageQuerySet.as_manager()

    BUILD_SUCCESS = True
    BUILD_FAILED = False
    BUILD_IMAGE_SUCCESS_CHOICES = [
        (BUILD_SUCCESS, 'Success'), (BUILD_FAILED, 'Failed')
    ]

    image_name = models.CharField(max_length = 100, )
    image_tag = models.CharField(max_length = 100, )
    build_image_result = models.TextField(null = True, default = None)
    build_image_success = models.IntegerField(null = False, default = BUILD_FAILED, choices = BUILD_IMAGE_SUCCESS_CHOICES)

    class Meta:
        unique_together = (('image_name', 'image_tag'),)

    def __str__(self):
        return f"<DockerImage object {self.id}> {self.image_name} - {self.image_tag} build: {self.build_image_success}"
