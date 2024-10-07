from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'complete'
    ]

    fieldsets = [
        (None, {'fields': ['user']}),
        ('To Do', {'fields': ['title']}),
        ('Task Details', {'fields': ['description', 'complete']}),
        ('Date Information', {'fields': ['date_created']}),
    ]

    list_filter = ['date_created']

    search_fields = ['title']


admin.site.register(Task, TaskAdmin)
