from django.db import models


class Games(models.Model):  # Список игры
    image = models.ImageField(upload_to='games/image/', null=True)
    title = models.CharField(max_length=200, verbose_name='Название игры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игру'
        verbose_name_plural = 'Игры'
