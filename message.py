import requests
sp = ""
for i in range(15):
    sp = sp + "spam\n"
payload = {
    'content' : str(sp)
}
#authorisation of the post request
header = {
    'authorization' : 'XXXXXXX'
}
#Get the target channel api
r = requests.post("api/channel",data=payload,headers=header)