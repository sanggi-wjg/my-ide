# MY-IDE

## Linux 환경
```shell
Ubuntu 20.04 Python 3.x 설치

# docker 설치
apt install docker.io  

# docker.sock 권한 설정
ln -s /var/run/docker.sock  /var/run/docker_www.sock
chown www:www /var/run/docker_www.sock
```

## Database 세팅
```shell
python manage.py migrate
```

![1](https://github.com/sanggi-wjg/my-ide/blob/main/docs/images/1.png?raw=true)

![2](https://github.com/sanggi-wjg/my-ide/blob/main/docs/images/2.png?raw=true)