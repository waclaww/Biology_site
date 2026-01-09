from django.contrib import admin
from .models import Article, Task

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display=("id", "title",)
    list_display_links=("id", "title",)
    search_fields=("id", "title",)

admin.site.register(Article, ArticleAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display=("id", "title",)
    list_display_links=("id", "title",)
    search_fields=("id", "title",)

admin.site.register(Task, TaskAdmin)