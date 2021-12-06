import logging

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class DockerIndexView(View):

    def get(self, request, **kwargs):
        return render(request, 'docker/index.html')


class CodeRunView(View):

    def post(self, request, **kwargs):
        response = requests.post(
            url = 'http://localhost:5000/run',
            data = { 'code': request.POST.get('code') }
        )

        try:
            result = response.json()
            result['error'] = result['error'].replace("\n", "<br>")
        except ValueError:
            result = response.text

        return JsonResponse({ 'data': result })
