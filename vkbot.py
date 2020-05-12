from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import requests
import vk_api
import random

token ='ae75ea73cf3c85e5476823346af0c68d9dccdc64183a3152882eb129f2c6078bc0e783751194172464381'
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:		
        if event.text == 'Как дела?' or event.text == 'Как настроение?': 
            if event.from_user: 
                vk.messages.send( 
                    user_id=event.user_id,
                    message='Отлично. А у тебя?')
            elif event.from_chat: 
                vk.messages.send(
                    chat_id=event.chat_id,
                    message='Отлично. А у тебя?')
for event2 in longpoll.listen():
    if event2.type == VkEventType.MESSAGE_NEW and event2.to_me and event2.text:		
        if event2.text == 'Что делаешь?' or event2.text == 'Чем занимаешься?': 
            if event2.from_user: 
                vk.messages.send( 
                user_id=event2.user_id,
                message='Смотрю фильм, посоветовать тебе крутые фильмы?')
            elif event2.from_chat: 
                vk.messages.send(
                    chat_id=event2.chat_id,
                    message='Смотрю сериал, посоветовать тебе крутые сериалы?')
for event2 in longpoll.listen():
    if event2.type == VkEventType.MESSAGE_NEW and event2.to_me and event2.text:		
        if event2.text == 'Да' or event2.text == 'Давай': 
            if event2.from_user: 
                vk.messages.send( 
                user_id=event2.user_id,
                message='Мстители, Призрак оперы, Завтрак у Тиффани')
            elif event2.from_chat: 
                vk.messages.send(
                    chat_id=event2.chat_id,
                    message='Черное зелкало, Игра Престолов, Шерлок Холмс')
                
                break
        continue


