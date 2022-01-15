from django.test import TestCase

from dockers.models import DockerImage
from dockers.module.docker_vo import DockerJson


class DockersModelsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_docker_image_create(self):
        # given
        docker_json = DockerJson("language", "version", 0)

        # when
        image = DockerImage.objects.publish(docker_json)

        # then
        self.assertEqual(image.build_image_result, None, "Image Build 결과는 None")
        self.assertEqual(image.build_image_success, False, "Image Build 성공 여부는 False")
        self.assertEqual(image.container_is_running, False, "Image Container Running 여부는 False")
