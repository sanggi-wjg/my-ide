from django.urls import path

from dockers.views import DockerIndexView

urlpatterns = [
    path("", DockerIndexView.as_view(), name = 'get-docker-index'),
]
