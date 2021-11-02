from django.contrib import admin
from .models import Api

# Register your models here.
class ApiAdmin(admin.ModelAdmin):
    list_display = ('id','personal_id','bot_link')
    list_display_links = ('id', 'personal_id','bot_link')

admin.site.register(Api, ApiAdmin)