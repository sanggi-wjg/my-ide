import logging

from dockers.models import DockerImage
from dockers.module.docker_client import MyDockerClient
from dockers.module.docker_utils import get_dockerfile_path
from dockers.module.docker_vo import DockerfileInfo, Dockers


def crate_dockerfile_info(image_name: str, image_tag: str) -> DockerfileInfo:
    dirpath, filepath = get_dockerfile_path(f"{image_name}-{image_tag}")
    dockerfile_info = DockerfileInfo(dirpath, filepath, image_name, image_tag)
    return dockerfile_info


def try_build_dockerfile(data: Dockers):
    # get dockerfile info
    image = DockerImage.objects.publish(data.image_name, data.image_tag)
    dockerfile_info = crate_dockerfile_info(image.image_name, image.image_tag)
    logging.info(f"Dockerfile Info : {dockerfile_info}")

    # build dockerfile
    client = MyDockerClient()
    result = client.build_dockerfile(dockerfile_info)

    # Check success or fail, then update.
    is_success = client.is_exist_docker_image_by_name(f"{image.image_name}-{image.image_tag}")
    DockerImage.objects.update_build_image_result(image.id, ''.join(result), is_success)
    logging.info(f"Try Build Dockerfile : {is_success}\n{result}")


def try_run_docker_image(data: Dockers):
    client = MyDockerClient()
    client.create_container_and_run()
