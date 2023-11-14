import json
import  urllib.request
from urllib.parse import urlencode, quote_plus
import os

import time

from dotenv import load_dotenv, find_dotenv

with open('prob-cbr-data\data\FB122\entities.dict','r' ) as entities:
    entities = entities.read()

entities = entities.split('\n')

fb_ids = []

for entity in entities:
    try:
        fb_id = entity.split('\t')[1]
        fb_ids.append(fb_id)
    except:
        continue


dotenv_path = find_dotenv() 
load_dotenv(dotenv_path)

API_KEY = os.environ.get('API_KEY')

names = {}
natalia_natalia = {}

count = 1

for id in fb_ids:

    print(f'---  {count} / {len(fb_ids)}  ---')
    query = id
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'ids':id,
        'limit': 10,
        'indent': True,
        'key': API_KEY
    }
    url = service_url + '?' + urlencode(params, quote_via=quote_plus)
    try:
        response = json.loads(urllib.request.urlopen(url).read())
    except:
        time.sleep(30)
        response = json.loads(urllib.request.urlopen(url).read())

    try:
        names[id] = response['itemListElement'][0]['result']['name']
    except:
        natalia_natalia[id] = response
    
    if count % 10  == 0:
        with open('./traduciones_entidades.json', 'w') as traducciones:
            json.dump(names,traducciones , indent=4)

        with open('./response_error.json', 'w') as errores:
            json.dump(natalia_natalia, errores, indent=4)
            
    count +=1
