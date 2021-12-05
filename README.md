# MY-IDE

## Install and usage

```shell
python manage.py migrate
```

### Issue

* 어떤 이미지 사용할 수 있는지 디비에 넣어 놓아야 하나?

```shell
dockers.json 읽음
-> commands / build_dockerfiles Dockerfile 빌드 시도
-> commands / run_docker_image Docker image 런 시도, 성공이면 DockerImage 업데이트
-> 
```

* 디비 컨테이너 자동으로 만들려면 어떻게 해야 할까?

```shell
python docker api 사용하자
https://docs.docker.com/language/python/build-images/
```

* 컨테이너 안에 코드는 어떻게 실행하지?

```shell
Python 3.8 경우
HTTP POST localhost:5000/run 시도
Response retreive   
```

## ETC

### Model

```shell
python manage.py makemigrations dockers
python manage.py sqlmigrate dockers 0001
python manage.py migrate
```

### docker.sock

```shell
ln -s /var/run/docker.sock  /var/run/docker_www.sock
chown www:www /var/run/docker_www.sock
```