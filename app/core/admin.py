from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('Personal Info'), {
            'fields': ('name', )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
        (_('Important dates'), {
            'fields': ('last_login', )
        }),
    )

    # this is from docs for custom User field, for create a new user
    # None is the title
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('email', 'password1', 'password2')
    }), )


# this uses custom
admin.site.register(models.User, UserAdmin)
# just need to register tag because you just want basic, default from model CRUD
admin.site.register(models.Tag)
admin.site.register(models.Ingredient)
