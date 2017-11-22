import requests
import json

url = "15.119.204.172"
username = "Administrator"
password = "password@123"

# create session
reqpath = u'/rest/v1/SessionService/Sessions'
body = { "UserName": username, "Password": password }
body = json.dumps(body)
content_length = len(body)
headers = {'Connection': 'Keep-Alive', 'Content-Type': u'application/json', 'Content-Length': str(content_length), 'Accept': '*/*'}
r = requests.post("https://"+url+reqpath, verify=False,data=body, headers=headers)
token = r.headers['x-auth-token']
print(token)
print("------------------------------------------------------------------")

# send reset request
reqpath = u'/rest/v1/Systems/1'
body = {"Action": "Reset","ResetType": "ForceRestart"}
body = json.dumps(body)
print (body)
post_headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}
print (post_headers)
print ("https://"+url+reqpath)
r = requests.post("https://"+url+reqpath, verify=False, data=body, headers=post_headers)
json_format = r.json()

print(r.text)
print(r.status_code)
