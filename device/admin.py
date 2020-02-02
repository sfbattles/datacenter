from django.contrib import admin

# Register your models here.
from . models import DeviceType
from . models import Device
from . models import DeviceManufacturer
from . models import DeviceInventory
from . models import DeviceDetail

admin.site.register(DeviceType)
admin.site.register(Device)
admin.site.register(DeviceManufacturer)
admin.site.register(DeviceInventory)
admin.site.register(DeviceDetail)