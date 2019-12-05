# print all status code for 100 users
# wants a function for each get put post delete - each function will write to local json file
# post will need input data
# login/login unsuccessful - post
# user data in json file on the side.  so need to send that data.
# create functions that will read from and write to files.

import requests
import json

bURL = "https://reqres.in/api/users/"
uURL = []

# below is the patch function
def patch_reqres(filename,url):
    f1 = open(filename,"r")
    f1Data = json.load(f1)
    PatchReq = requests.patch(pURL,f1Data)
    print(PatchReq.text)
    print(PatchReq.status_code)
    print(PatchReq.json())
    f1.close()
    return PatchReq

# here we use the patch function
filename = "patch.json"
pURL = "https://reqres.in/api/users/2"

print (patch_reqres(filename,pURL))

