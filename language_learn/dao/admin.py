from django.contrib import admin
from .models import AdvUser, Course


@admin.register(Course)
class Cource(admin.ModelAdmin):
    list_display = ("title",)



@admin.register(AdvUser)
class Cource(admin.ModelAdmin):
    list_display = ("username", "email",)
    search_fields = ("username",)
