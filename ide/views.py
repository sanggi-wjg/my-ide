from django.shortcuts import render

from django.views import View


class WebIdeIndexView(View):
    template_name = 'ide/index.html'

    def get(self, request):
        return render(request, self.template_name, {

        })
