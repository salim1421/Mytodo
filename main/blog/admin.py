from django.contrib import admin

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'date_created',
    ]

    fieldsets = [
        (None, {'fields':['author']}),
        ('Post Detail', {'fields': [
            'image',
            'title',
            'content',
            'category',
            'snippet',
            'likes',
        ]}),
        ('Date Information', {'fields': ['date_created']})
    ]

    list_filter = ['date_created']

    search_fields = ['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
