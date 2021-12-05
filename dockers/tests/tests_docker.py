from django.test import TestCase


class DockerTestCase(TestCase):
    """
    python manage.py test dockers.tests.tests_docker
    """

    def test_build_dockerfile(self):
        from docker import APIClient
        from my_ide.settings import DOCKERFILES_ROOT

        image_name, tag = 'python', '3.8'
        dockerfile_dir = f"{DOCKERFILES_ROOT}/{image_name}-{tag}"
        dockerfile_path = f"{dockerfile_dir}/Dockerfile"

        client = APIClient(base_url = 'unix://var/run/docker_www.sock')
        response = [line for line in client.build(
            path = dockerfile_dir, dockerfile = dockerfile_path,
            rm = True, tag = f"{image_name}-{tag}"
        )]

        for r in response:
            print(r)


def test_run_container():
    pass
