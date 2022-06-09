from django.db import models


class MainMenu(models.Model):  # главное меню
    mm_name = models.CharField(max_length=200, verbose_name='Название раздела')
    mm_link = models.CharField(max_length=200, verbose_name='Алиас', null=True)

    def __str__(self):
        return self.mm_name

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Главное Меню"
