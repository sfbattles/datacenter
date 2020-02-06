from django.contrib import admin

# Register your models here.
from . models import DeviceType
from . models import Device
from . models import DeviceManufacturer
from . models import DeviceInventory
from . models import DeviceDetail
from . models import PortSpeed
from . models import PortType
from . models import PortFunction

admin.site.register(DeviceType)
admin.site.register(Device)
admin.site.register(DeviceManufacturer)
admin.site.register(DeviceInventory)
admin.site.register(DeviceDetail)
admin.site.register(PortSpeed)
admin.site.register(PortType)
admin.site.register(PortFunction)