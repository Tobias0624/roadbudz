import csv
import os 
from strainSearch.models import strains

def run():
    files = open('/Users/adebolaadeyeye/Python~Django/weedApp/scripts/cannabis.csv')
    read_file = csv.reader(files)

    strains.objects.all().delete()

    count = 1

    for s in read_file:
        if count == 1:
            pass
        else:
            print(s)
            strains.objects.create(strainName=s[0], strainType=s[1], strainRating=s[2], strainEffefts=s[3], strainFlavor=s[4], strainDescription=s[5])
        count = count + 1