from django.http import HttpResponse

def HelloWorld(request):
    return HttpResponse("Hello World!!")