from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from Test.models import Test

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name="Заголовок")
    content = RichTextUploadingField(verbose_name="Контент")
    test = models.ForeignKey(Test, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Привязанный тест')
    
    def __str__(self):
        return f"{self.id}.{self.title}"
    
    def get_absolute_url(self):
        return reverse('article', kwargs={"id": self.id})
    
    class Meta:
        verbose_name="Статья"
        verbose_name_plural="Статьи"
        ordering=["id",]
        
class Task(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name="Заголовок задачи")
    condition = RichTextUploadingField(verbose_name="Условие задачи")
    solution = models.CharField(max_length=200, blank=False, verbose_name="Решение")
    
    def __str__(self):
        return f"{self.id}.{self.title}"
    
    def get_absolute_url(self):
        return reverse('condition', kwargs={"id": self.id})
    
    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"
        ordering=["id",]
        
        