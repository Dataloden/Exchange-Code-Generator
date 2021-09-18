import subprocess
import requests
import json
import os
import time
from random import seed
from random import randint

print("you can get an Authorization Code by going to https://www.epicgames.com/id/api/redirect?clientId=3446cd72694c4a4485d81b77adbb2141&responseType=code")
initialAuth = input("Please Enter Authorization Code:")

def get_access_token(authcode):
    url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"
    myobj = {'grant_type': 'authorization_code', 'code': authcode}
    x = requests.post(url, data = myobj, auth=('3446cd72694c4a4485d81b77adbb2141', '9209d4a5e25a457fb9b07489d313b41a'))
    tokentext = x.text
    texas = json.loads(tokentext)
    token = texas["access_token"]
    return token
   
def get_exchange_code(bearerToken):
    url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange"
    myobj = {'grant_type': 'authorization_code'}
    x = requests.get(url, data = myobj, headers={"Authorization": f"Bearer {bearerToken}"})
    tokentext = x.text
    texas = json.loads(tokentext)
    token = texas["code"]
    return token
    
key = get_access_token(initialAuth)
exchangeCode = get_exchange_code(key)
print(f"your Exchange Code is : {exchangeCode}")