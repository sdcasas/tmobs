from django.contrib import admin

from . import models, forms


@admin.register(models.Redirect)
class Redirect(admin.ModelAdmin):
    form = forms.RedirectForm
    list_display = ('key', 'url')
    list_filter = ('url', )
    search_fields = ('key', 'url')
    #readonly_fields = ['created_at', 'updated_at']
