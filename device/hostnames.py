import csv, os

from device.models import DeviceHostName

file_loc = '/home/richl/dev/source/datacenter/hosts.csv'
counter = 0
print (file_loc)
with open(file_loc, "r", encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    print(reader)
    for row in reader:     
        if row['Host'].strip():
            print("Value" +  row['Host'].strip()) 
            hostname_obj, created = DeviceHostName.objects.get_or_create(name=row['Host'])
            if created:
                # p = DeviceHostName(name=row['Host'])
                hostname_obj.save()
            