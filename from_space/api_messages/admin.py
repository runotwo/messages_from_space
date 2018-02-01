from django.contrib import admin
from .models import Message


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'text', 'is_read')
    list_filter = ('id', 'date', 'text', 'is_read')
    search_fields = ('text',)
    ordering = ['id']

admin.site.register(Message, PostAdmin)
