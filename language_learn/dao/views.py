from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import TemplateDoesNotExist


def index_dao(request):
    return render(request, "dao/main.html")


# выход на другие статичные страницы сайта
def other_page(request, page):
    try:
        template = get_template("dao/" + page + ".html")
    except TemplateDoesNotExist:
        # print("---------- request ------------")
        # print(request)
        # print("---------- dir(request) ------------")
        # print(dir(request))
        # print("---------- request.GET ------------")
        # print(request.GET)
        # print("---------- page ------------")
        # print(page)
        # print("---------- dir(page) ------------")
        # print(dir(page))
        # print()
        raise Http404
    return HttpResponse(template.render(request=request))
