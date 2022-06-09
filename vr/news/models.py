from django.db import models


class News(models.Model):  # Список новостей
    image = models.ImageField(upload_to='news/image/')
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
