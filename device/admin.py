from django.contrib import admin

# Register your models here.
from . models import DeviceType
from . models import Device

admin.site.register(DeviceType)
admin.site.register(Device)