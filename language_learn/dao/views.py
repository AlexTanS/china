from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.core.signing import BadSignature

from .models import *
from .forms import RegisterUserForm
from .utilities import signer


# основная страница сайта
def index_dao(request):
    return render(request, "dao/main.html")


# выход на другие статичные страницы сайта
def other_page(request, page):
    try:
        template = get_template("dao/" + page + ".html")
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


# страница курсы
def course(request):
    data = list()
    for datum in list(Course.objects.order_by("-rating")):
        d = list()
        d.append(datum.title)
        d.append(datum.content)
        d.append(datum.price)
        d.append(datum.rating)
        data.append(d)
    # data.sort(key=lambda x: -x[3])  # сортировка по назначенному рейтингу
    return render(request, "dao/course.html", context={"data": data})


# страница входа пользователя
class DaoLoginView(LoginView):
    template_name = "dao/login.html"


# выход пользователя
class DaoLogoutView(LoginRequiredMixin, LogoutView):  # LoginRequiredMixin - только зарегистрированным пользователям
    template_name = "dao/logout.html"


# страница личного кабинета
@login_required  # доступен только зарегистрированым пользователям
def profile(request):
    return render(request, "dao/profile.html")


# регистрация пользователя
class DaoRegisterUserView(CreateView):
    model = AdvUser
    template_name = "dao/register_user.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("register_done")


# вывод об успешности регистрации пользователя
class DaoRegisterDoneView(TemplateView):
    template_name = "dao/register_done.html"


# активация пользователя
def user_activate(request, sign):
    """
    :param sign: подписанный идентификатор пользователя, ктр. приходит в составе интерент-адреса
    :return: страница об удачной или нет активации пользователя
    """
    try:
        username = signer.unsign(sign)  # извлекаем из идентификатора логин пользователя
    except BadSignature:
        return render(request, "dao/bad_signature.html")
    user = get_object_or_404(AdvUser, username=username)  # извлекаем пользователя по логину
    if user.is_activated:
        template = "dao/user_is_activated.html"
    else:
        template = "dao/activation_done.html"
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)
