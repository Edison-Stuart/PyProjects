# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=import-error
# pylint: disable=unused-import

from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')


# Register your models here.
admin.site.register(Post, PostAdmin)
