from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal
from .utilities import send_activation_notification

user_registrated = Signal(providing_args=["instance"])


class AdvUser(AbstractUser):
    """Модель пользователей."""

    is_activated = models.BooleanField(default=True, db_index=True, verbose_name="Прошел активацию?")
    send_messages = models.BooleanField(default=True, verbose_name="Присылать оповещения?")
    courses = models.ManyToManyField("Course", blank=True, related_name="users")  # связь с курсами

    class Meta:
        verbose_name_plural = "Список пользователей"
        verbose_name = "пользователя"



class Progress(models.Model):
    """Прогресс обучения в играх."""
    game = models.PositiveSmallIntegerField(verbose_name="Номер игры")
    part_game = models.PositiveSmallIntegerField(verbose_name="Часть в игре")
    is_status = models.BooleanField(default=False, verbose_name="Играл ли в эту игру?")
    assessment = models.BooleanField(default=False, verbose_name="Прошел ли игру (оценка)?")
    user = models.ForeignKey(AdvUser, on_delete=models.PROTECT)

    class Meta:
        pass


class Course(models.Model):
    """Описание курсов."""
    title = models.CharField(max_length=255, verbose_name="Курс",
                             help_text="Наименование курса (не более 255 букв)")  # название курса
    # img = models.ImageField(upload_to="/media/", height_field=150, width_field=200,
    #                         verbose_name="Фото")  # иллюстрация курса (фото)
    content = models.TextField(verbose_name="Описание",
                               help_text="На пишите текст который будет отображаться на сайте - краткое описание")  # описание курса (текст)
    price = models.IntegerField(verbose_name="Стоимость в копейках",
                                help_text="Стоимость курса обучения в копейках для простоты расчетов")  # цена курса в копейках
    rating = models.SmallIntegerField(verbose_name="Рейтинг",  # рейтинг курса (влияет на отображение на сайте)
                                      help_text="Чем больше цифра тем выше он на сайте показывается")
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name="Дата публикации")  # дата публикации

    class Meta:
        verbose_name_plural = "База курсов"
        verbose_name = "курс обучения"
        ordering = ["rating"]


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs["instance"])


user_registrated.connect(user_registrated_dispatcher)
