import csv, os

from device.models import DeviceHostName

file_loc = '/home/richl/dev/source/datacenter/Savvis_switch.txt'
print (file_loc)
with open(file_loc, "r", encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter="\t")
    print(reader)
    for row in reader:     
        patch_obj, created = PatchPort.objects.get_or_create(number=row['patch'])   # check database if exists and created object if it doesn't
        host_obj, created = DeviceHostName.objects.get_or_create(name=row['Host']) 
        switch_label_obj, created = SwitchLabel.objects.get_or_create(name=row['Switch']) 
        switch_port_obj, created = Switch_Port.objects.get_or_create(port_number=row['Switch_Port']) 
        p = Port(device_hostname=host_obj,
                 device_description=row['Description'],
                 patch_port=patch_obj,
                 switch_port=switch_port_obj,
                 )
 p = Agent(agent_no=row['agent_no'],
        
        agent_master_code = agent_master_obj,
        name=row['name'],
        address=row['address'],
        city=row['city'],
        state=row['state'],
        zipcode=row['zipcode'],
        status=row['status'])
        p.save()




            