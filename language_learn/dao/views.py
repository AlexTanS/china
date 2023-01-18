from django.shortcuts import render
from django.http import HttpResponse


def index_dao(request):
    return render(request, "dao/index.html")
