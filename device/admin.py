from django.contrib import admin

from django.apps import apps

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

# from . models import DeviceType
# from . models import Device
# from . models import DeviceManufacturer
# from . models import DeviceInventory
# from . models import DeviceDetail
# from . models import DevicePurpose
# from . models import PortSpeed
# from . models import PortType
# from . models import PortFunction
# from . models import 

# # from . models import VLan

# admin.site.register(DeviceType)
# admin.site.register(Device)
# admin.site.register(DeviceManufacturer)
# admin.site.register(DeviceInventory)
# admin.site.register(DeviceDetail)
# admin.site.register(DevicePurpose)
# admin.site.register(PortSpeed)
# admin.site.register(PortType)
# admin.site.register(PortFunction)
# # admin.site.register(VLan)