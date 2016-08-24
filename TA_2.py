# CODE2040 
# TA 2: Reverse a string

# Written by: Andrea Jackson

import requests

url = "http://challenge.code2040.org/api/reverse"

token = 'c1a3396232e782e9b3db0ea03817e12d'

payload = {'token': token}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.post(url,json=payload, headers=headers)

string = response.content

# reverse the returned string
reverse_str = string[::-1]

validateURL = "http://challenge.code2040.org/api/reverse/validate"

payload2 = {'token':token,'string':reverse_str}

response2 = requests.post(validateURL,json=payload2,headers=headers)

print response2.content