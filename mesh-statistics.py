import urllib.request
import zipfile
import os

url = 'https://www.e-stat.go.jp/gis/statmap-search/data?statsId=T000876&code=3622&downloadType=2'

urllib.request.urlretrieve(url, 'output/sample.zip')

with zipfile.ZipFile('output/sample.zip') as zip:
    zip.extractall('output/')

os.remove('output/sample.zip')