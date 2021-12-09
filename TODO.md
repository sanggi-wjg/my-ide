## TODO

* [X] Docker build 와 Conatiner 처리는 어떻게?

```shell
0. dockerfieles / language-version / Dockerfile 작성
1. 사용할 dockers.json 작성
2. commands / build_dockerfiles Dockerfile 빌드 시도, 성공이면 DockerImage 업데이트 
3. commands / run_docker_images Docker image container 생성 및 실행, 성공이면 DockerImage 업데이트
(container id 같은거 받아서 저장하면 좋을 듯?)
```

* [X] Docker build 와 container 는 개발을 통해서 

```shell
python docker api 사용
https://docs.docker.com/language/python/build-images/

1. dockers / module
```

* [X] Docker Container 안에 코드 실행 방법

#### Python 3.8 경우
```shell
Flask 로 개발된 소스를 Dockerfile 로 빌드

이후 사용자 요청시에 Django 에서 
Flask Container 로 HTTP POST Request localhost:5000/run 
Response 를 view 로 retreive   
```

#### Python 2.7 경우
```shell
프레임 워크 없이 native 로 작성

docker container로 docker exec 실행하며 실행할때 arguements 로 코드를 전달 
native 소스에서 실행   
Response 를 view 로 retreive   
```


