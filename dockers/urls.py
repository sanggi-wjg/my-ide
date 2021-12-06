from django.urls import path

from dockers.views import DockerIndexView, CodeRunView

urlpatterns = [
    path("", DockerIndexView.as_view(), name = 'get-docker-index'),
    path("code-run", CodeRunView.as_view(), name = 'code-run'),
]
