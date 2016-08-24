# CODE2040 
# TA 4: Prefix

# Written by: Andrea Jackson

import requests
import ast
from collections import Counter 

url = "http://challenge.code2040.org/api/prefix"

token = 'c1a3396232e782e9b3db0ea03817e12d'

payload = {'token': token}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.post(url,json=payload, headers=headers)

stringDict = response.content
dictionary = ast.literal_eval(stringDict)

prefix = dictionary['prefix']
array = dictionary['array']

def findStrings(pre,arr):
    '''return an array containing only the 
    strings that do not start with prefix'''
    finalArray = []
    numLetters = len(pre) 
    for item in arr:
        # add the item if the Counters do not have the same values
        if (Counter(pre) != Counter(item[:numLetters])):
            finalArray.append(item)
    return finalArray
    
noPrefixArray = findStrings(prefix,array)

validateURL = "http://challenge.code2040.org/api/prefix/validate"

payload2 = {'token':token,'array':noPrefixArray}

response2 = requests.post(validateURL,json=payload2,headers=headers)

print response2.content