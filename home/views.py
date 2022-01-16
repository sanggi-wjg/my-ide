from django.shortcuts import render

from django.views import View


class HomeIndexView(View):
    page_title = 'Run Your Code!'
    template_name = 'home/index.html'

    def get(self, request):
        return render(request, self.template_name, { 'page_title': self.page_title })
