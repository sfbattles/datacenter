from device.models import PatchPort

# import csv, os

# file_loc = '/home/richl/dev/source/datacenter/port.csv'
# print (file_loc)
# with open(file_loc, "r", encoding='utf-8-sig') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter="|")
#     for row in reader:       
#         print(row['Port'])
#         p = SwitchPort(port_number=row['Port'])
#         p.save()

#         from device.models import SwitchPort

import csv, os

file_loc = '/home/richl/dev/source/datacenter/port.csv'
print (file_loc)
with open(file_loc, "r", encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    for row in reader:       
        print(row['Port'])
        # p = PatchPort(number=row['Port'])
        # p.save()