import vk_api
import datetime as dt
from threading import Thread, Timer
import emoji as moji
import time

def sender(user_id, text=''):       
    vk.messages.send(user_id = user_id, message = text, random_id = 0)

token = input('Access token: ')
session = vk_api.VkApi(token = token)
vk = session.get_api()

link = input('Link of user: ')
screen_name = link.split('/')[3]
user_id = vk.utils.resolveScreenName(screen_name=screen_name)['object_id']

count = int(input('Times to send messages: '))
text = input('Message text: ')

for i in range(count):
    sender(user_id, text)


