import requests
import json

def scrape_messages(channelID) :
    #auth key for the get request
    headers = {
        'authorisation' : "XXXXXX"
    }
    r = requests.get('api/{channelID}/messages' , headers=headers)
    data = json.loads(r.text)
    for msg in data : 
        print(msg + '\n')
targetChannelID = 'XXXX'
scrape_messages(targetChannelID)
