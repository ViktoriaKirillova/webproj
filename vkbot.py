from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import requests
import vk_api
import random
import wikipedia

token ='ae75ea73cf3c85e5476823346af0c68d9dccdc64183a3152882eb129f2c6078bc0e783751194172464381'
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
wikipedia.set_lang("RU")

if event.text == 'Википедия' or event.text == 'Вики' or event.text == 'википедия' or event.text == 'вики' or event.text == 'Wikipedia' or event.text == 'wikipedia' or event.text == 'Wiki' or event.text == 'wiki': 
    if event.from_user: 
        vk.messages.send(
            user_id=event.user_id,
            message='Введите запрос' 
	)
    elif event.from_chat: 
        vk.messages.send(
            chat_id=event.chat_id,
            message='Введите запрос' 
	)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text: 
            if event.from_user:
                vk.messages.send( 
                    user_id=event.user_id,
                    message='Вот что я нашёл: \n' + str(wikipedia.summary(event.text)) )
                break
        elif event.from_chat: 
            vk.messages.send(
                chat_id=event.chat_id,
                message='Вот что я нашёл: \n' + str(wikipedia.summary(event.text)))
            break 
    continue


