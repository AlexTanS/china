from django.db import models


class ContentBase(models.Model):
    """Тексты для страниц."""
    title = models.CharField(max_length=255, verbose_name="Заголовок")  # заголовок
    content = models.TextField(null=True, blank=True, verbose_name="Текст")  # текст
    # TODO Поле для рубрик из другой таблицы rubrics
    # TODO Поле для фотографии models.ImageField
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата публикации")  # дата публикации

    class Meta:
        verbose_name_plural = "База текстов для обычных страниц сайта"
        verbose_name = "текст обычной страницы сайта"
        ordering = ["-published"]

# class Rubrics(models.Model):
#     """Рубрики."""
#     rubric = models.CharField(max_length=255, verbose_name="Рубрика")
#
#     class Meta:
#         verbose_name_plural = "Рубрики"
#         verbose_name = "рубрика"
#         ordering = ["rubrics"]

# class Courses(models.Model):
#     """Описание крусов."""
#     title = models.CharField(max_length=255, verbose_name="Курс")  # название курса
#     img = models.ImageField(upload_to="/media/", height_field=150, width_field=200, verbose_name="Фото")  # иллюстрация курса (фото)
#     content = models.TextField(null=True, blank=True, verbose_name="Описание")  # описание курса (текст)
#     price = models.DecimalField(null=True, blank=True, verbose_name="Стоимость")  # цена курса
#     discount = models.DecimalField(null=True, blank=True, verbose_name="Скидка")  # скидка (коэфициент на который умножается цена)
#     rating = models.IntegerField(max_length=255, verbose_name="Рейтинг")  # рейтинг курса (влияет на отображение на сайте)
#     published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата публикации")  # дата публикации
#
#     class Meta:
#         verbose_name_plural = "База курсов"
#         verbose_name = "курс обучения"
#         ordering = ["rating"]
