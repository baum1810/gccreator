import requests, json, time
from os import system
def cls():
    system("cls")
    
token1 = input("Token\n> ")    
def gettoken(token1):
    cls()
    
    headers = {
        'Authorization': token1,
        'Content-Type': 'application/json'
    }
    
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    
    if res.status_code == 200:
        pass
       
    else: 
        cls()
        print("Invalid token pls try another one")
        time.sleep(3)
        gettoken(token1)
gettoken(token1)

headers = {
    'Authorization': token1,
    'Content-Type': 'application/json'
}

res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)

if res.status_code == 200:
                res_json = res.json()
                id1 = res_json['id']


id2 = input("Target id\n> ")




while True:
    
    
    headers = {
    'Authorization' : token1,
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.308 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'
    }
    
    requests.post('https://discordapp.com/api/v9/users/@me/channels', headers=headers, json={"recipients":[id1, id2]})