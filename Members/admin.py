from django.contrib import admin
from .models import *

# Register your models here.

class ResultAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id", "user")
    ordering = ("id",)
    
admin.site.register(Result, ResultAdmin)