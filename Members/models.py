from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

class Result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, verbose_name="Пользователь")
    test = models.ForeignKey('Test.Test', blank=False, on_delete=models.PROTECT, verbose_name="Тест")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name='Дата создания')
    rightAnswers = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Правильные ответы')
    wrongAnswers = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Неправильные ответы')
    questions = models.IntegerField(validators=[MinValueValidator(0)], default=0, verbose_name='Всего вопросов')

    def str(self):
        return f'{self.id}. {self.test}'

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
        ordering = ['-created_at', '-test']