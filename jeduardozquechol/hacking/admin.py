from django.contrib import admin
from .models import Hacking

# Register your models here.
class HAckingAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Hacking, HAckingAdmin)