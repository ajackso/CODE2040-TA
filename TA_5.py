# CODE2040 
# TA 5: The dating game

# Written by: Andrea Jackson

import requests
import ast
import datetime

url = "http://challenge.code2040.org/api/dating"

token = 'c1a3396232e782e9b3db0ea03817e12d'

payload = {'token': token}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.post(url,json=payload, headers=headers)

stringDict = response.content
dictionary = ast.literal_eval(stringDict)

datestamp = dictionary['datestamp']
interval = dictionary['interval']

def sumDatetime_Seconds(dateS,seconds):
    '''returns the sum of an ISO 8601 datestamp
    and seconds as an ISO 8601 datestamp string'''
    
    # use strftime to parse ISO 8601 datestamp string into
    # a datetime object
    datetime_time = datetime.datetime.strptime(dateS,"%Y-%m-%dT%H:%M:%SZ")
    #print "datetime_time: " + str(datetime_time)
    
    datetime_delta = datetime.timedelta(seconds=seconds)
    #print "datetime_delta: " + str(datetime_delta)
    
    # sum times
    totalTime = datetime_time + datetime_delta
    #print "totalTime: " + str(totalTime)
    
    # convert datetime object back to ISO 8601 datestamp
    # add UTC time
    UTC_time = "Z"
    return totalTime.isoformat()+UTC_time 

#print sumDatetime_Seconds("2016-09-03T10:35:56Z",260715)

finalDatestamp = sumDatetime_Seconds(datestamp,interval)

validateURL = "http://challenge.code2040.org/api/dating/validate"

payload2 = {'token':token,'datestamp':finalDatestamp}

response2 = requests.post(validateURL,json=payload2,headers=headers)

print response2.content