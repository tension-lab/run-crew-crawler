import json
import os

import requests

BASE = 'https://www.runcrewfinder.com'
API = BASE + '/api/crew/getsAll.json'
OUTPUT_PATH = 'output'

res = requests.post(API, headers={'content-type': 'application/json'}, data='{"selectOrderType":"find","crewName":""}')

data = json.loads(res.text)

if not os.path.isdir(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

for crew in data['data']['list']:
    file_name = crew['crewName'] + '.' + crew['logoFileUrl'].split('.')[-1]

    logo_res = requests.get(BASE + crew['logoFileUrl'])
    with open(os.path.join(OUTPUT_PATH, file_name), 'wb') as f:
        f.write(logo_res.content)
