import urllib.request
import zipfile
import os
import time
import csv
import glob

meshes = []

with open('mesh-code.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        meshes.append(row)

for mesh in meshes:
    url = 'https://www.e-stat.go.jp/gis/statmap-search/data?statsId=T000876&code=%s&downloadType=2' % mesh

    urllib.request.urlretrieve(url, 'output/temporary/_.zip')

    with zipfile.ZipFile('output/temporary/_.zip') as zip:
        zip.extractall('output/temporary')

    os.remove('output/temporary/_.zip')

    time.sleep(0.5)

temps = glob.glob('output/temporary*')

print(temps)

'''
with open('open.csv', 'a') as output:
    pass
'''
