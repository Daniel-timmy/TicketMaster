from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

from .models import Creator


# Register your models here.
class CreatorAdmin(UserAdmin):
    """

    """
    model = Creator
    list_display = ['email', 'company_name', 'name', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('id', 'email', 'password')}),
        ('Personal Info', {'fields': ('company_name', 'name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'company_name', 'name', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


# class CustomLogEntry(LogEntry):
#     user_uuid = models.UUIDField(_('user UUID'), blank=True, null=True)
#
#     class Meta:
#         verbose_name = _('log entry')
#         verbose_name_plural = _('log entries')


admin.site.register(Creator, CreatorAdmin)
# admin.site.register(CustomLogEntry)
