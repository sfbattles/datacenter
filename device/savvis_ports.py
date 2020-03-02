import csv, os

from device.models import DeviceHostName
from device.models import Switch
from device.models import PatchPort
from device.models import SwitchPort
from device.models import Port

file_loc = '/home/richl/dev/source/datacenter/savvis_switch.txt'
print (file_loc)
with open(file_loc, "r", encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter="\t")
    print(reader)
    for row in reader:     
        patch_obj, created = PatchPort.objects.get_or_create(number=row['patch_port'])   # check database if exists and created object if it doesn't
        host_obj, created = DeviceHostName.objects.get_or_create(name=row['host'])  
        switch_name_str = row['switch']
        print(switch_name_str)
        the_switch_obj = Switch.objects.get(name=switch_name_str)       
        switch_port_obj, created = SwitchPort.objects.get_or_create(port_number=row['switch_port'])
        
        p = Port(
            device_hostname = host_obj,
            device_description = row['description'],
            patch_port = patch_obj,
            switch_port = switch_port_obj,
            switch = the_switch_obj)
        p.save()




            