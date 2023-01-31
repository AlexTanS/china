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
        raise Http404
    return HttpResponse(template.render(request=request))
