# syntax=docker/dockerfile:1

FROM    python:2.7-slim-buster
WORKDIR /app
COPY    . .

ENTRYPOINT ["tail", "-f", "/dev/null"]

# docker build -t python-2.7 .
# docker run -d --name python-2.7 python-2.7