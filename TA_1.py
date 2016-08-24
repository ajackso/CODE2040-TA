# CODE2040 
# TA 2: Register

# Written by: Andrea Jackson

import requests

url = "http://challenge.code2040.org/api/register"

token = 'c1a3396232e782e9b3db0ea03817e12d'

payload = {'token': token}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.post(url,json=payload, headers=headers)

print response.content