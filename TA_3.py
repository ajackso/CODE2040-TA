# CODE2040 
# TA 3: Needle in a haystack

# Written by: Andrea Jackson

import requests
import ast 

url = "http://challenge.code2040.org/api/haystack"

token = 'c1a3396232e782e9b3db0ea03817e12d'

payload = {'token': token}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.post(url,json=payload, headers=headers)

stringDict = response.content
hDict = ast.literal_eval(stringDict)

needle = hDict['needle']
haystack = hDict['haystack']

def findIndex(n,h):
    '''returns the index of n in list h. returns -1 if n is not in list h'''
    if n in h:
        return h.index(n)
    else:
        return -1

index = findIndex(needle,haystack)

validateURL = "http://challenge.code2040.org/api/haystack/validate"

payload2 = {'token':token,'needle':index}

response2 = requests.post(validateURL,json=payload2,headers=headers)

print response2.content