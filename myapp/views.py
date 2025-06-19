from django.http import HttpResponse

def home(request):
    response = HttpResponse('elcome to my app home')
    return response