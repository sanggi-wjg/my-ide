from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class DockerIndexView(View):

    def get(self, request, **kwargs):
        return render(request, 'docker/index.html')
