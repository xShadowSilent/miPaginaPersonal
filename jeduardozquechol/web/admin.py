from django.contrib import admin
from .models import Web

# Register your models here.
class WebAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Web, WebAdmin)