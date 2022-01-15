import os.path

from django.test import TestCase

from dockers.models import DockerImage
from dockers.module.docker_service import crate_dockerfile_info
from dockers.module.docker_utils import read_dockerfiles_dir_files, walk_dockerfiles_dir_get_filenames
from dockers.module.docker_vo import DockerJson


class ReadDockerfilesTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def create_docker_json_python38(self):
        return DockerJson("python", "3.8", 8000)

    def create_docker_json_python27(self):
        return DockerJson("python", "2.7", 0)

    def setUp(self) -> None:
        # docker_json = self.create_docker_json_python27()
        # image = DockerImage.objects.publish(docker_json)
        # self.docker_image = image
        pass

    def tearDown(self) -> None:
        pass

    def test_read_dockerfiles_python38(self):
        # given
        docker_json = self.create_docker_json_python38()
        image = DockerImage.objects.publish(docker_json)

        dockerfile_info = crate_dockerfile_info(image)
        dirpath = dockerfile_info.dirpath

        # when
        # files = walk_dockerfiles_dir_get_filenames(dirpath)
        # print(files)
        files_read_result = read_dockerfiles_dir_files(dirpath)
        for k, v in files_read_result.items():
            print(k, v)

        # then
        self.assertEqual(dirpath, "/home/my-ide/dockerfiles/python-3.8", "dockerfiles 경로")
        # self.assertIsInstance(files_read_result, dict, "files_read_result 는 dict")

    def test_read_dockerfiles_python27(self):
        # given
        docker_json = self.create_docker_json_python27()
        image = DockerImage.objects.publish(docker_json)

        dockerfile_info = crate_dockerfile_info(image)
        dirpath = dockerfile_info.dirpath

        # when
        # files = walk_dockerfiles_dir_get_filenames(dirpath)
        # print(files)
        files_read_result = read_dockerfiles_dir_files(dirpath)
        for k, v in files_read_result.items():
            print(k, v)

        # then
        self.assertEqual(dirpath, "/home/my-ide/dockerfiles/python-2.7", "dockerfiles 경로")
        self.assertIsInstance(files_read_result, dict, "files_read_result 는 dict")


class ExecuteCodeTestCase(TestCase):
    """
    python manage.py test docker.tests.tests_util
    """

    def test_code_execute(self):
        from io import StringIO
        import sys

        code_output = StringIO()
        code_error = StringIO()
        sys.stdout = code_output
        sys.stderr = code_error

        sample_code = "print('hello world')"
        exec(sample_code)

        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        print(f"error: {code_error.getvalue()}")
        print(f"output: {code_output.getvalue()}")
