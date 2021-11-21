import requests
import random
import threading
token1 = "YOUTOKEN"
threads = 30


def rename(token1):
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", 
    headers={"Authorization": token1}).json()
    
    
    
    for channel in channelIds:
        Ran = ''.join(random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcbnm123456789') for i in range(7))
        headers = {
        'authorization': token1,
        
        
        }
        
        payload = {
            "name":Ran
        }
        
        r = requests.put(f"https://discord.com/api/v9/channels/{channel['id']}", headers=headers, json=payload)
        
for i in range(threads):
    t = threading.Thread(target=rename(token1))
    t.start()  
