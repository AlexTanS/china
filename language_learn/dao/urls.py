from django.urls import path

from .views import index_dao

urlpatterns = [
    path("", index_dao),
]