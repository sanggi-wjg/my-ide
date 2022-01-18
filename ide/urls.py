from django.urls import path

from ide import views

urlpatterns = [
    path("web-ide", views.WebIdeIndexView.as_view(), name = 'get-web-ide-index'),
]
