from django.urls import path

from .views import index_dao, other_page

urlpatterns = [
    path("", index_dao, name="index_dao"),
    path("<page>/", other_page, name="other"),  # выход на другие статичные страницы сайта
]