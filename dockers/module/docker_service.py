import logging

from dockers.models import DockerImage
from dockers.module.docker_client import MyDockerClient
from dockers.module.docker_utils import get_dockerfile_path
from dockers.module.docker_vo import DockerfileInfo, DockerJson


def crate_dockerfile_info(image: DockerImage) -> DockerfileInfo:
    dirpath, filepath = get_dockerfile_path(f"{image.image_name}-{image.image_tag}")
    dockerfile_info = DockerfileInfo(dirpath, filepath, image.image_name, image.image_tag)
    return dockerfile_info


def build_dockerfile(docker_json: DockerJson):
    # get dockerfile info
    image = DockerImage.objects.publish(docker_json)
    dockerfile_info = crate_dockerfile_info(image)

    # build dockerfile
    client = MyDockerClient()

    # if is build in the past, do not build again
    is_built = client.is_exist_docker_image_by_name(f"{image.image_name}-{image.image_tag}")
    if not is_built:
        # try build
        built_image, built_result = client.build_dockerfile(dockerfile_info)
        # print('id:', built_image.id, 'tags:', built_image.tags, 'labels:', built_image.labels)

        # Check success or fail, then update.
        is_built = client.is_exist_docker_image_by_name(f"{image.image_name}-{image.image_tag}")
        DockerImage.objects.update_build_image_result(image.id, built_result, is_built)
        if not is_built:
            logging.error(f"{dockerfile_info} build failed")
    else:
        logging.info(f"{dockerfile_info} is already built")


def run_docker_image(image: DockerImage):
    client = MyDockerClient()
    is_success = client.create_container_and_run(image)
    DockerImage.objects.update_container_running_result(image.id, is_success)
