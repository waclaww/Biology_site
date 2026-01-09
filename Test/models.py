from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='tests/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    is_random = models.BooleanField(default=False, verbose_name='Перемешать?')
    amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)], default=10, verbose_name='Количество вопросов', help_text='Если вопросов привязанных к тесту больше чем указано в поле "Количество вопросов", то система случайным образом выберет указанное количество вопросов.')
    
    def get_absolute_url(self):
        return reverse('test', kwargs={'id': self.id})

    def __str__(self):
        return f"{self.id}. {self.title}"
    
    def get_questions(self):
        return Question.objects.filter(test__id=self.id)
    
    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
        ordering = ["id",]

class Question(models.Model):
    title = models.CharField(max_length=500, blank=False, verbose_name='Вопрос')
    photo = models.ImageField(upload_to='question_images/full_test/%Y/%m/%d', blank=True, verbose_name='Изображение')
    answer1 = models.CharField(max_length=500, blank=True, verbose_name="Ответ 1")
    answer2 = models.CharField(max_length=500, blank=True, verbose_name="Ответ 2")
    answer3 = models.CharField(max_length=500, blank=True, verbose_name="Ответ 3")
    answer4 = models.CharField(max_length=500, blank=True, verbose_name="Ответ 4")
    right_answer = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(4),
    ], default=1, verbose_name='Правильный ответ')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, blank=False, verbose_name='Входит в тест')
    
    def __str__(self):
        return f"{self.id}: {self.title}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["id",]
    