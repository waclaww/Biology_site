from django.contrib import admin
from .models import *

# Register your models here.

class TestAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    list_display_links = ("id", "title",)
    ordering = ("id",)
    
admin.site.register(Test, TestAdmin)



















class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "test")
    list_display_links = ("id", "title", "test")
    list_filter = ("test",)
    ordering = ("id",)
    
admin.site.register(Question, QuestionAdmin)