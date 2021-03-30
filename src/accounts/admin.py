from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User


class UserAdmin(BaseUserAdmin):

    add_fieldsets = [
        (None, {'fields': ['email', 'password1', 'password2', 'user_type']})
    ]
    list_display = ('email', 'created_at', 'last_modified', 'user_type', )
    readonly_fields = ('created_at', 'last_modified', 'password')
    list_filter = ['user_type']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Metadata', {'fields': ('created_at', 'last_modified', 'user_type')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
