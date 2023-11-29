# open and read a specific url x
# print that we are retrieving the url x
# print the amount of characters in url x
# create a new dictionary for the value and have it sum the key and the values to get sum and counter

import urllib.request, urllib.error, urllib.parse
import json
html = input('Enter WebPage Here: ')
print('Retrieving ' + html)
jsn = urllib.request.urlopen(html)
data = jsn.read()
print ('Retrieved ' + str(len(data)) + ' characters')
dicto = json.loads(data)
lst = list()
count = 0

for i in dicto['comments']:
    count += 1
    iner = i['count']
    lst.append(iner)
print(count)
print(sum(lst))
