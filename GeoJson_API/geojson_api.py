import urllib.request, urllib.error, urllib.parse
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = line.strip()

pari = {}
pari['address'] = address
if api_key is not False: pari['key'] = api_key
url = serviceurl + urllib.parse.urlencode(pari)

print('Retrieving ', url)
new_url = urllib.request.urlopen(url, context=ctx)
data = new_url.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

print(js['results'][0]['place_id'])

