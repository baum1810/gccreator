import requests, json

token1 = "TOKEN"




channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", 
headers={"Authorization": token1}).json()
for channel in channelIds:
    
    header = {
    'authorization': token1
    
    }

    r = requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers=header)   
