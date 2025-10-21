from django.contrib import admin

from .models import Task

@admin.register(Task)  
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'data')
    list_filter = ('completed', 'data')
    search_fields = ('title', 'description')
