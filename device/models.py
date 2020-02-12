from django.db import models

class DeviceType(models.Model):
    type = models.CharField(max_length=250)

    class Meta:
        verbose_name = "DeviceType"
        verbose_name_plural = "DeviceTypes"
        db_table = 'DeviceType'

    def __str__(self):
        return str(self.type)

class DeviceRackLocation(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "DeviceRackLocation"
        verbose_name_plural = "DeviceRackLocation"
        db_table = 'DeviceRackLocation'

    def __str__(self):
        return str(self.name)


# Primary or seconday
class DevicePurpose(models.Model):
    type = models.CharField(max_length=250)

    class Meta:
        verbose_name = "DevicePurpose"
        verbose_name_plural = "DevicePurpose"
        db_table = 'DevicePurpose'

    def __str__(self):
        return str(self.type) 

#LAN, SFP, Console, Management 
class PortFunction(models.Model):
    function = models.CharField(max_length=250)

    class Meta:
        verbose_name = "PortFunction"
        verbose_name_plural = "PortFunction"
        db_table = 'PortFunction'

    def __str__(self):
        return str(self.function)


# class VLan(models.Model):
#     number = models.PositiveSmallIntegerField()
#     description = models.CharField(max_length=250)

#     class Meta:
#         verbose_name = "VLan"
#         verbose_name_plural = "VLans"
#         db_table = 'VLan'

#     def __str__(self):
#         return str(self.number) + " " + self.description
                                 
# megabit, gigabit
class PortType(models.Model):
    type = models.CharField(max_length=250)

    class Meta:
        verbose_name = "PortType"
        verbose_name_plural = "PortTypes"
        db_table = 'PortType'

    def __str__(self):
        return str(self.type)


# 1, 10, 40, 100
class PortSpeed(models.Model):
    speed = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "PortSpeed"
        verbose_name_plural = "PortSpeed"
        db_table = 'PortSpeed'

    def __str__(self):
        return str(self.speed)


class DeviceManufacturer(models.Model):
    name =  models.CharField(max_length=250)

    class Meta:
        verbose_name = "DeviceManufacturer"
        verbose_name_plural = "DeviceManufacturer"
        db_table = 'DeviceManufacturer'

    def __str__(self):
        return str(self.name)

class DeviceDetail(models.Model):
    device_manufacturer = models.ForeignKey(DeviceManufacturer,  
        on_delete = models.CASCADE) 
    item_detail = models.CharField(max_length=250)

    class Meta:
        verbose_name = "DeviceDetails"
        verbose_name_plural = "DeviceDetails"
        db_table = 'DeviceDetail'

    def __str__(self):
        return str(self.device_manufacturer) + " " + self.item_detail


class DeviceInventory(models.Model):
    manufacturer = models.ForeignKey(DeviceManufacturer, on_delete=models.CASCADE)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    device_detail = models.ForeignKey(DeviceDetail, on_delete=models.CASCADE,default="")
    # serial_number = models.CharField(max_length=50)
    # service_tag = models.CharField(max_length=50)   
    # express_service_code = models.CharField(max_length=50)  
    # mac_address = models.CharField(max_length=50)
    # description = models.CharField(max_length=250)
    # device_type_id = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    # number_of_rack_unit = models.PositiveSmallIntegerField()    
    # device_model = models.CharField(max_length=502,default="")   #model number of device
    
    class Meta:
        verbose_name = "DeviceInventory"
        verbose_name_plural = "DeviceInventory"
        db_table = 'DeviceInventory'

    def __str__(self):
        return str(self.manufacturer)


class Device(models.Model):
    device_inventory_id = models.ForeignKey(DeviceInventory, on_delete=models.CASCADE)
    starting_rack_unit_position = models.PositiveSmallIntegerField()
    ending_rack_unit_position = models.PositiveSmallIntegerField()
    rack_id = models.PositiveIntegerField()
    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"
        db_table = 'Device'

    def __str__(self):
        return str(self.device_inventory_id)