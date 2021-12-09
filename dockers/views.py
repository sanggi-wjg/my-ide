import requests
from django.http import JsonResponse
from django.shortcuts import render

from django.views import View

from dockers.module.docker_client import MyDockerClient


class DockerIndexView(View):

    def get(self, request, **kwargs):
        return render(request, 'docker/index.html')


class DockerCodeRunView(View):

    def post(self, request, **kwargs):
        user_language = request.POST.get('user_language')
        user_code = request.POST.get('user_code')

        result = request_result(user_language, user_code)
        print(result)
        return JsonResponse({ 'data': result })


def request_result(user_language: str, user_code: str):
    if user_language == 'Python3.8':
        return request_python3_result(user_code)
    elif user_language == 'Python2.7':
        client = MyDockerClient()
        return client.exec_run_container('python-2.7', f"python /app/app.py '{user_code}'")
    else:
        raise Exception('Not allowed language')


def request_python3_result(user_code: str):
    response = requests.post(
        url = 'http://localhost:5000/run',
        data = { 'code': user_code }
    )

    try:
        result = response.json()
        print(result)
        result['error'] = result['error'].replace("\n", "<br>")
    except ValueError:
        result = response.text

    return result
