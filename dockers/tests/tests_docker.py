from unittest import skipIf

from django.test import TestCase


class DockerTestCase(TestCase):
    """
    python manage.py test dockers.tests.tests_docker
    """

    def test_build_dockerfile(self):
        from dockers.module.docker_client import MyDockerClient
        from my_ide.settings import DOCKERFILES_ROOT
        from dockers.module.docker_vo import DockerfileInfo

        image_name, image_tag = 'python', '3.8'
        dockerfile_info = DockerfileInfo(
            f"{DOCKERFILES_ROOT}/{image_name}-{image_tag}",
            f"{DOCKERFILES_ROOT}/{image_name}-{image_tag}/Dockerfile",
            image_name, image_tag
        )
        client = MyDockerClient()
        result = client.build_dockerfile(dockerfile_info)
        print(result)

    @skipIf(True, 'tested')
    def test_get_docker_image_by_name(self):
        from dockers.module.docker_client import MyDockerClient
        name = 'python-3.8'
        client = MyDockerClient()
        result = client.get_docker_image_by_name(name)

        self.assertTrue(result)

    # def test_run_docker_image(self):
    #     import docker
    #     target = 'python-3.8'
    #
    #     client = docker.DockerClient(base_url = 'unix://var/run/docker_www.sock')
    #     container = client.api.create_container(
    #         image = target, detach = True, name = target,
    #         ports = [5000, ],
    #         host_config = client.api.create_host_config(port_bindings = {
    #             5000: ('127.0.0.1', 5000)
    #         })
    #     )
    #     client.api.start(container.get('Id'))
