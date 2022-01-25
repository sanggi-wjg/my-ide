import logging

from dockers.models import DockerImage
from dockers.module.docker_client import MyDockerClient
from dockers.module.docker_utils import get_dockerfile_path
from dockers.module.docker_vo import DockerfileInfo, DockerJson


def crate_dockerfile_info(image: DockerImage) -> DockerfileInfo:
    dirpath, filepath = get_dockerfile_path(image.image_fullname)
    return DockerfileInfo(dirpath, filepath, image.image_name, image.image_tag)


def build_dockerfile(docker_json: DockerJson):
    # get dockerfile info
    image = DockerImage.objects.publish(docker_json)
    dockerfile_info = crate_dockerfile_info(image)

    # build dockerfile
    # if is build in the past, do not build again
    client = MyDockerClient()
    is_exist_image = client.is_exist_docker_image_by_name(image.image_fullname)

    if not is_exist_image:
        # try build
        built_image, built_result = client.build_dockerfile(dockerfile_info)
        # print('id:', built_image.id, 'tags:', built_image.tags, 'labels:', built_image.labels)

        # Check success or fail, then update.
        is_built = client.is_exist_docker_image_by_name(image.image_fullname)
        if is_built:
            DockerImage.objects.update_build_image_result_success(image.id, built_result)
        else:
            DockerImage.objects.update_build_image_result_failed(image.id, built_result)
            logging.error(f"{dockerfile_info} build failed")
    else:
        logging.info(f"{dockerfile_info} is already built")


def run_docker_image(image: DockerImage):
    client = MyDockerClient()
    is_success = client.create_container_and_run(image)

    if is_success:
        DockerImage.objects.update_container_running_success(image.id, is_success)
    else:
        DockerImage.objects.update_container_running_failed(image.id, is_success)
