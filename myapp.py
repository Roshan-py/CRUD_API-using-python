import requests
import json
from PIL import Image
import os

URL = "http://127.0.0.1:8000/crud_api/"


def get_data(id=None):
    data={}
    if id is not None:
        data= {'id':id}
    json_data= json.dumps(data)
    headers= {'content-Type':'application/json'}
    r= requests.get(url=URL,headers=headers, data=json_data)
    data=r.json()

    print(data)


#get_data()


def post_data():
    data={
        'name':'ravi',
        'img':'https://lh3.googleusercontent.com/OGQkzkYdfhAXE6p-xufS_6mB3MtjDfPM6HZPdDrX5uJ09Dh1vzLZ6YflPIduh2Jk-h7H',
        'summery': 'hello world'
    }

    json_data = json.dumps(data)
    headers={'content-Type':'application/json'}
    r = requests.post(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

post_data()

def update_data():
    data={
        'id':1,
        'name':'neha'
    }

    json_data = json.dumps(data)
    headers={'content-Type':'application/json'}
    r = requests.put(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)


#update_data()


def delete_data():
    data={'id':3}

    json_data = json.dumps(data)
    headers={'content-Type':'application/json'}
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


#delete_data()