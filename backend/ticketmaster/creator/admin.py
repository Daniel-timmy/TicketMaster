from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Creator


# Register your models here.
class CreatorAdmin(UserAdmin):
    """

    """
    model = Creator
    list_display = ['id', 'email', 'company_name', 'name', 'is_staff', 'is_active']
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


admin.site.register(Creator, CreatorAdmin)
