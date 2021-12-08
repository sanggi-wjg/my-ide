### Model
```shell
python manage.py makemigrations dockers
python manage.py sqlmigrate dockers 0001
python manage.py migrate
```

### docker.sock
```shell
# add symbolic link of docker.sock
ln -s /var/run/docker.sock  /var/run/docker_www.sock
chown www:www /var/run/docker_www.sock
```

### Ref
```shell
https://docker-py.readthedocs.io/en/stable/
```