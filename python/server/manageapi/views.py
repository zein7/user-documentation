from django.conf.urls import include, url
from django.core import management
from django.views.generic import View
from django.http import JsonResponse
from io import StringIO

class ManageDotApi(View):
    """
    Probably the worst idea in the history of bad ideas
    """
    
    def get(self, request, *args, **kwargs):
        command = self.kwargs['command']
        # try:
        #     API_KEY = os.getenv("DJANGO_MANAGE_API_KEY")
        # except:
        #     return JsonResponse({
        #     'command': command,
        #     "error": "API Key not given"
        # })
        args = self.request.GET.getlist("arg")
        command_kwargs = dict(self.request.GET)
        # if API_KEY != self.request.GET.getlist("arg")
        out = StringIO()
        err = StringIO()

        management.call_command(command, stdout=out, stderr=err, *args, **command_kwargs)
        return JsonResponse({
            'command': command,
            "stdout": out.getvalue(),
            "stderr": err.getvalue(),
        })