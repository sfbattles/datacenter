from django.db import models

# switch or Router
class DeviceType(models.Model):
    type = models.CharField(max_length=250)

    class Meta:
        verbose_name = "DeviceType"
        verbose_name_plural = "DeviceTypes"
        db_table = 'DeviceType'

    def __str__(self):
        return str(self.type)


class Rack(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Rack"
        verbose_name_plural = "Rack"
        db_table = 'Rack'

    def __str__(self):
        return str(self.name)


class DataCenter(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "DataCenter"
        verbose_name_plural = "DataCenter"
        db_table = 'DataCenter'

    def __str__(self):
        return str(self.name)

# Primary or Seconday
class DeviceRole(models.Model):
    role = models.CharField(max_length=250)

    class Meta:
        verbose_name = "DeviceRole"
        verbose_name_plural = "DeviceRole"
        db_table = 'DeviceRole'

    def __str__(self):
        return str(self.role)

# LAN, SFP, Console, Management 
class PortFunction(models.Model):
    function = models.CharField(max_length=250)

    class Meta:
        verbose_name = "PortFunction"
        verbose_name_plural = "PortFunction"
        db_table = 'PortFunction'

    def __str__(self):
        return str(self.function)

                                 
# megabit, gigabit
class PatchPort(models.Model):
    number = models.CharField(max_length=250)

    class Meta:
        verbose_name = "PatchPort"
        verbose_name_plural = "PatchPort"
        db_table = 'PatchPort'

    def __str__(self):
        return str(self.number)


# gigabit or megabits
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


class DeviceHostName(models.Model):
    name =  models.CharField(max_length=250)

    class Meta:
        verbose_name = "DeviceHostName"
        verbose_name_plural = "DeviceHostName"
        db_table = 'DeviceHostname'

    def __str__(self):
        return str(self.name)


# the  Switch label in the cabnet
class SwitchLabel(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "SwitchLabel"
        verbose_name_plural = "SwitchLabel"
        db_table = 'SwitchLabel'

    def __str__(self):
        return str(self.name)


class SwitchPort(models.Model):
    port_number = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "SwitchPort"
        verbose_name_plural = "SwitchPort"
        db_table = 'SwitchPort'

    def __str__(self):
        return str(self.port_number)


# default to switch SWITCH = ID 1
# null=True, blank=True  if you want this field optional
DEFAULT_DEVICE_TYPE = 1
DEFAULT_ROLE_TYPE = 1
class Switch(models.Model):
    manufacturer = models.ForeignKey(DeviceManufacturer, on_delete=models.CASCADE)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, default=DEFAULT_DEVICE_TYPE)
    device_role = models.OneToOneField(DeviceRole, on_delete=models.CharField, default=DEFAULT_ROLE_TYPE)   #primary or secondary switch
    data_center = models.OneToOneField(DataCenter, on_delete=models.CharField,null=True, blank=True)
    rack = models.OneToOneField(Rack, on_delete=models.CharField,null=True, blank=True)
    name = models.ForeignKey(SwitchLabel, on_delete=models.CASCADE,null=True, blank=True) 
    # port = models.ForeignKey(Port, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Switch"
        verbose_name_plural = "Switch"
        db_table = 'Switch'

    def __str__(self):
        return str(self.manufacturer) + " " + str(self.device_type)

class Port(models.Model):
    device_hostname = models.ForeignKey(DeviceHostName,on_delete=models.CASCADE,null=True, blank=True) 
    device_description = models.CharField(max_length=250, null=True, blank=True)
    patch_port = models.ForeignKey(PatchPort, on_delete=models.CASCADE,null=True, blank=True)    
    switch_port = models.ForeignKey(SwitchPort, on_delete=models.CASCADE, null=True, blank=True) 
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Port"
        verbose_name_plural = "Port"
        db_table = 'Port'

    def __str__(self):
        return str(self.device_hostname)