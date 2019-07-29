import requests
import urllib3
import json
urllib3.disable_warnings()
sessionID = ""

#Specify username, password, and FMG IP
username = "json"
password = "123456"
BaseURL = 'https://172.31.200.57/jsonrpc'

#Base template for making API calls
def json_template(sessionID):
    Params = {
        "session": sessionID
    }

    requests.post(url=BaseURL, json=Params, verify=False)
    
#Function: Creates new Address object with type subnet
#Usage: 
#   Specify Address object settings under "data" parameter
#   Url parameter needs to specify your ADOM name
def add_firewall_address(sessionID):
    Params =  {
        "method": "add",
        "session": sessionID,
        "id": 1,
        "params": [{
            "data": [{
                "associated-interface": "any",
                "color": 1,
                "comment": "",
                "name": "h_10.123.123.123",
                "subnet": [ "10.123.123.123", "255.255.255.255" ],
                "type": 0,
                #"url": "",
                "visibility": 1 
            }],
            "url": "/pm/config/adom/54/obj/firewall/address"
        }]
    }
    requests.post(url=BaseURL, json=Params, verify=False)

#not used anymore
def json_edit_address(sessionID):
    address_table = []
    
    print("Changing addresses...")
    for x in range(1, 301):
        for y in range (1,11):
            address_table.append({
                "data": {
                    "subnet": "10.10.0.7 255.255.255.255",
                },
                "url": "/pm/config/adom/Hybrids/obj/firewall/address/IPS"+str(y)+"-Host"+str(x)
            })

    # address_table.append({
    #     "data": {
    #         "subnet": "10.0.0.5 255.255.255.255",
    #     },
    #     "url": "/pm/config/adom/Hybrids/obj/firewall/address/IPS1-Host1"
    # })

    EditAddressParams = {
        "method": "set",
        "params": address_table,
        "session": sessionID,
        "id": 1
    }

    #Change Request
    requests.post(url=BaseURL, json=EditAddressParams, verify=False)

#Function: login to API and store session in variable "sessionID"
#DO NOT MODIFY    
def json_login(username, password):
    global sessionID
    LoginParams = {
        "id": 1, 
        "method": "exec", 
        "params": [
            {
                "data": [
                    {
                        "passwd": password, 
                        "user": username
                    }
                ], 
            "url": "sys/login/user"
            }
        ], 
        "session": None, 
        "verbose": 1
    }

    #Login Request
    resp = requests.post(url=BaseURL, json=LoginParams, verify=False)

    #Store Login Session ID
    json_data = json.loads(resp.text)
    #print(resp.text)
    print("Logged in! Session ID: " + json_data["session"])
    sessionID = json_data["session"]

#Function: Logs out of existing session
#DO NOT MODIFY
def json_logout(sessionID):
    LogoutParams = {
        "id": 1, 
        "jsonrpc": "1.0", 
        "method": "exec", 
        "params": [
            {
                "url": "sys/logout"
            }
        ], 
        "session": sessionID,
        "verbose": 1
    }

    #Logout Request
    requests.post(url=BaseURL, json=LogoutParams, verify=False)
    print("Logged out :)")

json_login(username, password)
#---------Do stuff here---------

add_firewall_address(sessionID)

#---------No more stuff---------
json_logout(sessionID)