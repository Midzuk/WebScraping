import urllib.request
import zipfile
import os
import time
import csv
import glob

filename = input('filename: ')

#header_num = int(input('header number: '))

#statsID = input('statsID: ')

temps = glob.glob('output/temporary/*')

for temp in temps:
    os.remove(temp)

meshes = []

#with open('mesh-code.csv', 'r') as f:
#    meshes = sum(csv.reader(f), [])

with open('mesh-code.csv', 'r', encoding="utf-8") as f:
    meshes = sum(csv.reader(f), [])

#meshes = [str(y) + str(x) for y in range(36, 69) for x in range(22, 49)]
#meshes_exist = []

for mesh in meshes:
    url = 'https://www.e-stat.go.jp/gis/statmap-search/data?dlserveyId=Q&code=%s&coordSys=1&format=shape&downloadType=5' % mesh

    try:
        urllib.request.urlretrieve(url, 'output/temporary/_.zip')

        with zipfile.ZipFile('output/temporary/_.zip') as zip:
            zip.extractall('output/temporary')

        os.remove('output/temporary/_.zip')

        time.sleep(0.2)

    except:
        print('Mesh %s is not exist' % mesh)

#for temp in temps:
#   os.remove(temp) 
