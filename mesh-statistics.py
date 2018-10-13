import urllib.request
import zipfile
import os
import time
import csv
import glob

filename = input('filename: ')

header_num = int(input('header number: '))

'''
statsID = input('statsID: ')

temps = glob.glob('output/temporary/*')

for temp in temps:
    os.remove(temp)

meshes = []

with open('mesh-code.csv', 'r') as f:
    meshes = sum(csv.reader(f), [])

#meshes = [str(y) + str(x) for y in range(36, 69) for x in range(22, 49)]
#meshes_exist = []

for mesh in meshes:
    url = 'https://www.e-stat.go.jp/gis/statmap-search/data?statsId=%s&code=%s&downloadType=2' % (statsID, mesh)

    try:
        urllib.request.urlretrieve(url, 'output/temporary/_.zip')

        with zipfile.ZipFile('output/temporary/_.zip') as zip:
            zip.extractall('output/temporary')

        os.remove('output/temporary/_.zip')

        time.sleep(0.2)

    except:
        print('Mesh %s is not exist' % mesh)

'''
temps = glob.glob('output/temporary/*')

with open('output/%s.csv' % filename, 'w', encoding='cp932') as f:
    writer = csv.writer(f, lineterminator = '\n')

    with open(temps[0], 'r', encoding = 'cp932') as t0:
        reader = csv.reader(t0)
        headers = []

        for _ in range(0, header_num):
            header = next(reader)
            headers.append(header)

        writer.writerows(headers)
    
    for temp in temps:
        with open(temp, 'r', encoding = 'cp932') as t:
            reader = csv.reader(t)
            for _ in range(0, header_num): 
                next(reader)
            writer.writerows(reader)

#for temp in temps:
#   os.remove(temp) 
