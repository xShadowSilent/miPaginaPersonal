from django.contrib import admin
from .models import Programacion

# Register your models here.
class ProgramacionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Programacion, ProgramacionAdmin)