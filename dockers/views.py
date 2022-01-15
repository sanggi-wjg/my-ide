import requests
from django.http import JsonResponse
from django.shortcuts import render

from django.views import View
from django.views.generic import ListView, DetailView

from dockers.models import DockerImage
from dockers.module.docker_client import MyDockerClient
from dockers.module.docker_service import crate_dockerfile_info
from dockers.module.docker_utils import read_dockerfiles_dir_files


class DockerListView(View):
    page_title = 'Docker list'
    template_name = 'docker/docker_list.html'

    def get(self, request):
        return render(request, self.template_name, {
            'page_title': self.page_title,
            'objects'   : DockerImage.objects.all(),
        })


class DockerDetailView(DetailView):
    model = DockerImage
    context_object_name = 'object'
    template_name = 'docker/docker_detail.html'
    pk_url_kwarg = 'image_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        dockerfile_info = crate_dockerfile_info(context[self.context_object_name])
        files_read_results = read_dockerfiles_dir_files(dockerfile_info.dirpath)

        context['dockerfile'] = files_read_results.get('Dockerfile', '')
        files_read_results.pop('Dockerfile')
        context['files'] = files_read_results

        return context


class DockerCodeRunView(View):

    def post(self, request):
        user_language = request.POST.get('user_language')
        user_code = request.POST.get('user_code')

        result = request_result(user_language, user_code)
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
