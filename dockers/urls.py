from django.urls import path

from dockers.views import DockerIndexView, DockerCodeRunView

urlpatterns = [
    path("", DockerIndexView.as_view(), name = 'get-docker-index'),
    path("code-run", DockerCodeRunView.as_view(), name = 'code-run'),
]
