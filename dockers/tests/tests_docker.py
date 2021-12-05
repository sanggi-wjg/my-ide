def test_build_dockerfile():
    from io import BytesIO
    from docker import APIClient

    f = BytesIO(dockerfile.encode('utf-8'))
    cli = APIClient(base_url = 'tcp://127.0.0.1:2375')


def test_build_image():
    pass


def test_run_container():
    pass
