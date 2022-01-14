from django.urls import path

from home import views

urlpatterns = [
    path("", views.HomeIndexView.as_view(), name = 'get-home-index'),
]
