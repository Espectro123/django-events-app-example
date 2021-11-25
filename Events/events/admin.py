from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, Subscription


class AdminEvent(admin.ModelAdmin):
    """Display the data of list_display on the tab Events in Django admin"""

    list_display = ['id', 'author', 'title_text']
    ordering = ['id', 'author', 'title_text']


class AdminSubscription(admin.ModelAdmin):
    """Display the data of list_display on the tab Subscription in Django admin"""

    list_display = ['id', 'username', 'comment']
    ordering = ['id', 'username', 'comment']


admin.site.register(Event, AdminEvent)
admin.site.register(Subscription, AdminSubscription)

