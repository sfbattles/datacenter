import csv, os

from device.models import PatchPort

file_loc = '/home/richl/dev/source/datacenter/port.csv'
print (file_loc)
with open(file_loc, "r", encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    for row in reader:       
        print(row['Port'])
        p = PatchPort(number=row['Port'])
        p.save()