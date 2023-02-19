from django.urls import path

from .views import *

urlpatterns = [
    path("", index_dao, name="index_dao"),
    path("<str:page>/", other_page, name="other"),  # выход на другие статичные страницы сайта
    path("accounts/login/", DaoLoginView.as_view(), name="login"),  # страница входа пользователя
    path("accounts/profile/", profile, name="profile"),  # страница личного кабинета пользователя
    path("accounts/logout/", DaoLogoutView.as_view(), name="logout"),  # выход пользователя

    # страница завершения регистрации
    path("accounts/register/done/", DaoRegisterDoneView.as_view(), name="register_done"),
    path("accounts/register/", DaoRegisterUserView.as_view(), name="register"),  # страница регистрации пользователя
    path("accounts/register/activate/<str:sign>/", user_activate, name="register_activate"),  # активация пользователя
    path("cources/", cources, name="cources"),  # страница курсы
]
