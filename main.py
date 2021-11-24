import requests, json, time, threading, random
from os import system
num_thread = int("300")  
def cls():
    system("cls")
token1 = input("Token\n> ")    


headers = {
"Authorization": token1
}
channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", 
headers={"Authorization": token1}).json()



for channel in channelIds:
            f = open("ids.txt", "a")
            f.write(f"{channel['id']}\n")
            f.close()
def gettoken(token1):
    system("cls")
    
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
cls()
choice = int(input("[1] create groups\n[2] show how many are loaded\n[3] add to groups\n[4] remove from groups\n> "))
cls()


def create(token1):
    def gettoken(token1):
        system("cls")
        
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
    
    counter = 0
    
    
    while True:
        
        k = cv2.waitKey(1) & 0xFF
        headers = {
        'Authorization' : token1,
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.308 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'
        }
        
        r = requests.post('https://discordapp.com/api/v9/users/@me/channels', headers=headers, json={"recipients":[id1, id2]})
        headers = {
        "Authorization": token1
        }
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", 
        headers={"Authorization": token1}).json()
        
        
        if r.status_code == 429:
            print("raidlimitet waiting 10 minutes")
            time.sleep(600)
        elif r.status_code == 200:
            
            counter = counter+1
            system("cls")
            test = r.json()
            r2 = requests.delete(f"https://discord.com/api/v9/channels/{test['id']}/recipients/{id2}", headers={"authorization": token1})
            f = open("ids.txt", "a")
            f.write(f"{test['id']}\n")
            f.close()
            print(f"Groups created: {counter}")
        if k == ord('q'):
            break

            
def counterg(token1):
    counter = 0
        
    file = open("ids.txt", "r")
    for line in file:
        counter = counter+1

    print(f"Groups loaded: {counter}")
    system("pause")
   
def addi(token1, id):
    

    
    with open("ids.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))    
    
    
    
        r = requests.put(f"https://discord.com/api/v9/channels/{random.choice(words)}/recipients/{id}", headers={"authorization": token1})    
        
        if r.status_code == 204:
            system("cls")

            print(f"Target added to groups")
    
def removi(token1, userid):
    
    
    
    with open("ids.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        

        r = requests.delete(f"https://discord.com/api/v9/channels/{random.choice(words)}/recipients/{userid}", headers={"authorization": token1})    
    print("sucessfull removed from all groups")

    
    
if choice == 1:
    create(token1)
elif choice == 2:
    counterg(token1)
elif choice == 3:
    id = input("Target id: ")
    system("cls")
    
    for i in range(num_thread):
        t = threading.Thread(target=addi(token1, id))
        t.start()    
    
elif choice == 4:
    userid = input("Target id: ")
    system("cls")
    
    for i in range(num_thread):
        t = threading.Thread(target=removi(token1, userid))
        t.start()    
    
else:
    system("cls")
    print("invalid option")
    
