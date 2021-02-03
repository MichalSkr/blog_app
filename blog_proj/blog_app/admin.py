from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Writer, Article


class WriterAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'password1', 'password2'),
        }),
    )

    list_display = ('name', 'first_name', 'last_name', 'is_staff')
    search_fields = ('name', 'first_name', 'last_name')
    ordering = ('name',)


class ArticleTemplate(admin.ModelAdmin):
    list_display = ('title', 'written_by')


admin.site.register(Writer, WriterAdmin)
admin.site.register(Article, ArticleTemplate)
