from django.db import models
from django.db.models import QuerySet


class DockerImageQuerySet(models.QuerySet):

    def publish(self, image_name: str, image_tag: str) -> QuerySet['DockerImage']:
        try:
            result = self.get(image_name = image_name, image_tag = image_tag)
        except DockerImage.DoesNotExist:
            result = self.create(image_name = image_name, image_tag = image_tag)
        return result

    def update_build_image_result(self, image_id: int, result):
        rows = self.filter(
            id = image_id
        ).update(
            build_image_result = result
        )
        return rows


class DockerImage(models.Model):
    objects = DockerImageQuerySet.as_manager()

    image_name = models.CharField(max_length = 100, )
    image_tag = models.CharField(max_length = 100, )
    build_image_result = models.TextField(null = True, blank = None)

    class Meta:
        unique_together = (('image_name', 'image_tag'),)

    def __str__(self):
        return f"<DockerImage object {self.id}> {self.image_name} - {self.image_tag}"
