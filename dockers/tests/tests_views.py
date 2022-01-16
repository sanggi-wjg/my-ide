import os.path

from django.test import TestCase

from common.utils import get_directories, validate_dir, id_generator
from dockers.models import DockerImage
from dockers.module.docker_service import crate_dockerfile_info
from dockers.module.docker_vo import DockerJson
from my_ide.settings import SNIPPET_ROOT


class SnippetsViewsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self) -> None:
        DockerImage.objects.publish(DockerJson("python", "3.8", 8000))
        DockerImage.objects.publish(DockerJson("python", "2.7", 8000))
        images = DockerImage.objects.all()

        self.dirpath = SNIPPET_ROOT
        self.dockerfile_infos = [crate_dockerfile_info(image) for image in images]

    def tearDown(self) -> None:
        pass

    def _create_source_folders(self):
        validate_dir(self.dirpath)
        for info in self.dockerfile_infos:
            dirpath = os.path.join(self.dirpath, f"{info.image_name}_{info.image_tag}")
            validate_dir(dirpath)
            print('Validate ', dirpath)

            for _ in range(5):
                rand_dirpath = os.path.join(dirpath, id_generator())
                validate_dir(rand_dirpath)
                print('Validate ', rand_dirpath)

    def test_get_source_folders(self):
        # self._create_source_folders()

        files = get_directories(self.dirpath)
        print(files)
