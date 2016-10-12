from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def callback(request):
    return HttpResponse()
