from django.db import models


class DockerImage(models.Model):
    image_name = models.CharField(max_length = 100, )
    tag = models.CharField(max_length = 100, )
