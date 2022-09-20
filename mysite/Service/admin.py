from django.contrib import admin
from Service.models import Services

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon' , 'service_title' , 'service_des')

admin.site.register(Services , ServiceAdmin)
# Register your models here.

