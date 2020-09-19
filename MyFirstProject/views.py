from django.http import HttpResponse
from django.shortcuts import render


def artem(request):
    return HttpResponse('Hello Ar!!!m. How are you?')

def home(request):
    return render(request, 'home.html', {'greeting' : 'hello'})