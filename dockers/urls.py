from django.urls import path

from dockers import views

urlpatterns = [
    path("search", views.DockerListView.as_view(), name = 'get-docker-list'),
    path("search/<int:image_id>", views.DockerDetailView.as_view(), name = 'get-docker-detail'),

    path("code-run", views.DockerCodeRunView.as_view(), name = 'post-docker-code-run'),
]
