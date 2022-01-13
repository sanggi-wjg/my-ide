from django.urls import path

from dockers import views

urlpatterns = [
    path("", views.DockerIndexView.as_view(), name = 'get-docker-index'),
    path("search", views.DockerSearchView.as_view(), name = 'get-docker-search'),
    path("code-run", views.DockerCodeRunView.as_view(), name = 'code-run'),
]
