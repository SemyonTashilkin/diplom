from django.db import models


class Faq(models.Model):  # Часто задаваемые вопросы
    faq_question = models.CharField(max_length=200, verbose_name='Вопрос')
    faq_answer = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return self.faq_question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
