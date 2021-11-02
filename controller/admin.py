from django.contrib import admin
from .models import Control
# Register your models here.

class ControlAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

admin.site.register(Control, ControlAdmin)