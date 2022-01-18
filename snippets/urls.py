from django.urls import path

from snippets import views

urlpatterns = [
    path("search", views.SnippetsSourceFolderView.as_view(), name = 'get-snippets-source-folder-list'),
]
