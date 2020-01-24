from django.db import models

class DeviceType(model.Model):
    type = models.CharField(max_length=250)
    name = models.CharField(max_length=500)
    class Meta:
        verbose_name = "DeviceType"
        verbose_name_plural = "DeviceTypes"
        db_table = 'DeviceType'

    def __str__(self):
        return str(self.type)

class Device(model.Model):
    device_type_id = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    rack_unit_size = models.PositiveSmallIntegerField()
    starting_rack_unit_position = Model.PositiveSmallIntegerField()
    snding_rack_unit_position = Model.PositiveSmallIntegerField()
    rack_id = Model.PositiveIntegerField()
    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"
        db_table = 'Device'

    def __str__(self):
        return str(self.device_type_id)