import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
import ssl

url = input('Enter URL Here: ')
print('Retrieving...',url)
counter = 0
list = list()
XML = urllib.request.urlopen(url)
data = XML.read()
print('Retrieved ' + str(len(data)) + ' characters')
tree = ET.fromstring(data)
count = tree.findall('.//count')

for i in count:
    counter = counter + 1
    inter = int(i. text)
    list.append(inter)
print(counter)
print(sum(list))

