from django.http import JsonResponse

from django.views import View

from my_ide.settings import SNIPPET_ROOT


class SnippetsSourceFolderView(View):
    dirpath: str = ''

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.dirpath = SNIPPET_ROOT

    def get(self, request):
        return JsonResponse({
            'msg': 'success'
        })

    def put(self, request):
        # Create & Modify(over write?)
        pass

    def delete(self, request):
        # Delete
        pass


class SnippetsSourceFileView(View):

    def put(self, request):
        # Create & Modify(over write?)
        pass
