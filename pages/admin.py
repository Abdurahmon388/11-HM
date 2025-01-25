from django.contrib import admin

from . import models

admin.site.register(models.ContactModel)


@admin.register(models.AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'job',)
    search_fields = ('name', 'job',)
    list_filter = ('job',) 