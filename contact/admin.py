from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date', 'is_read')
    list_filter = ('is_read', 'created_date')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_date',)
