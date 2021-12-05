# MY-IDE

## Install and usage

```shell
python manage.py migrate
```

### Issue

* 어떤 이미지 사용할 수 있는지 디비에 넣어 놓아야 하나?
* 디비 컨테이너 자동으로 만들려면 어떻게 해야 할까?
    * python docker api 사용하자
    * https://docs.docker.com/language/python/build-images/
* 컨테이너 안에 코드는 어떻게 실행하지?
    * 파이썬은 랜덤 유니크 파일명 파일 생성해서 돌리고 결과값 받을 수가 있을까? 


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