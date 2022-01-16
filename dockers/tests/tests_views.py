import os.path

from django.test import TestCase

from common.utils import validate_dir, id_generator, get_directories
from dockers.models import DockerImage
from dockers.module.docker_vo import DockerJson
from my_ide.settings import SNIPPET_ROOT


class SnippetsViewsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self) -> None:
        DockerImage.objects.publish(DockerJson("python", "3.8", 8000))
        DockerImage.objects.publish(DockerJson("python", "2.7", 8000))
        self.images = DockerImage.objects.all()

        self.dirpath_root = SNIPPET_ROOT

    def tearDown(self) -> None:
        pass

    def _create_source_folders(self):
        validate_dir(self.dirpath_root)
        for image in self.images:
            dirpath = os.path.join(self.dirpath_root, image.sub_folder_name)
            validate_dir(dirpath)
            print('Validate ', dirpath)

            for _ in range(5):
                rand_dirpath = os.path.join(dirpath, id_generator())
                validate_dir(rand_dirpath)
                print('Validate ', rand_dirpath)

    def test_get_source_folders(self):
        # given
        # self._create_source_folders()

        # when
        directories = get_directories(self.images, self.dirpath_root)
        print(directories)

        # then
        self.assertEqual(list(directories.keys()), ['python_3.8', 'python_2.7'])
