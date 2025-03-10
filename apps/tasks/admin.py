from django.contrib import admin
from .models import Task


class TasksAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    list_display = ('title', 'description', 'created_At', 'updated_At')


admin.site.register(Task, TasksAdmin)
