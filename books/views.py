from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "books/index.html")


def detail(request, name):
    context = {'name': name}
    return render(request, "books/detail.html", context)
