import requests

token1 = "YOURTOKEN"
userid = "USERIDTOKICK"

channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", 
   headers={"Authorization": token1}).json()
   
   
   
for channel in channelIds:
    r = requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}/recipients/{userid}", headers={"authorization": token1})
