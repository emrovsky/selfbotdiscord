import requests
import websocket
import json
import threading
import time

def send_message(token,channel_id,message):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    data = {
        "content": f"{message}"
    }
    header = {
        "authorization": f"{token}"
    }
    r = requests.post(url,headers=header,data=data)
    print(r.text)

def join_server(token,server_id):
    url = f"https://discord.com/api/v9/invites/{server_id}"
    header = {
        "authorization": f"{token}"
    }
    r = requests.post(url,headers=header)
    print(r.text)

def delete_message(token,channel_id,message_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}"
    header = {
        "authorization": f"{token}"
    }
    r = requests.delete(url,headers=header)
    print(r.text)

def edit_message(token,channel_id,message_id,message_content):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}"
    header = {
        "authorization": f"{token}"
    }
    data = {
        "content":f"{message_content}"
    }
    r = requests.patch(url, headers=header,data=data)
    print(r.text)

def typing(token,channel_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/typing"
    header = {
        "authorization": f"{token}"
    }
    r = requests.post(url,headers=header)
    print(r.text)
    print(f"Typing on {channel_id} id's channel")

def version():
    print("© Copyright by Emrovsky in 2021 v1")

def create_role_name_new_role(token,guild_id):
    url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
    header = {
        "authorization": f"{token}"
    }
    data = {
        "name":"new role"
    }
    r = requests.post(url,data=data,headers=header)
    print(r.text)

def logging_message(token):
    def send_json_request(ws, request):
        ws.send(json.dumps(request))

    def recieve_json_response(ws):
        response = ws.recv()
        if response:
            return json.loads(response)

    def heartbeat(interval, ws):
        print('Listening has started')
        while True:
            time.sleep(interval)
            heartbeatJSON = {
                "op": 1,
                "d": "null"
            }
            send_json_request(ws, heartbeatJSON)

    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
    event = recieve_json_response(ws)

    heartbeat_interval = event['d']['heartbeat_interval'] / 1000
    threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

    token = token
    payload = {
        'op': 2,
        "d": {
            "token": token,
            "properties": {
                "$os": "windows",
                "$browser": "chrome",
                "$device": 'pc'
            }
        }
    }
    send_json_request(ws, payload)

    while True:
        event = recieve_json_response(ws)

        try:
            print(f"{event['d']['author']['username']}: {event['d']['content']}")

            op_code = event['op']
            if op_code == 11:
                print('heartbeat received')
        except:
            pass

def send_friend_request(token,user_id):
    headers = {'Authorization': token}
    r = requests.put(f"https://discordapp.com/api/v9/users/@me/relationships/{user_id}", headers=headers,json={'content-type:': "application/json"})
    print("Friend request has been send!")

