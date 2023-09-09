import vk_api
from mytoken import token_id
from vk_api.longpoll import VkLongPoll, VkEventType
import keyboards
from vk_api.utils import get_random_id
from get_weather import get_weather_today
from get_weather import get_weather_tomorrow
from get_traffic import get_traffic
from get_currency import get_currency
from get_afisha import get_afisha_main

About
Python bot for vk.com. By entering city allows you to get a weather forecast for today and tomorrow, status of traffic jams in the city, top 5 currencies to ruble, top 5 events for today and tomorrow in the city

'''
Python bot for vk.com. By entering city allows you to get:
- a weather forecast for today and tomorrow
- status of traffic jams in the city
- top 5 currencies to ruble
- top 5 events for today and tomorrow in the city
'''

vk_session = vk_api.VkApi(token=token_id)
vk_api_access = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def send_message(id, text, keyboard=None):
    post = {
        'user_id':id,
        'message': text,
        'random_id': get_random_id()
    }
       
    if keyboard == '''{"one_time":false,"inline":false,"buttons":[]}''':
        post['keyboard'] = keyboard
    else:
        if keyboard is not None:
            post['keyboard'] = keyboard.get_keyboard()
        
    vk_session.method('messages.send', post)


def get_city(id):
    try:
        response = vk_session.method('users.get', {'user_ids': id, 'fields': 'city'})
        response = response[0]
        city = response.get('city').get('title')
        return city
    except AttributeError:
        return None
    

def get_name(id):
    response = vk_session.method('users.get', {'user_ids': id, 'fields': 'first_name'})
    response = response[0]
    name = response.get('first_name')
    return name if name else None

def change_city(id):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            new_city = event.text
            send_message(id, f'Ваш город {new_city.capitalize()}', keyboards.main_menu)
            return new_city
      
def yes_or_no(id,city):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text == "Да":
                send_message(id, f'Ваш город {city.capitalize()}', keyboards.main_menu)
                return city
            elif event.text == 'Нет':
                send_message(id, 'Введите ваш город', keyboards.start.get_empty_keyboard())
                typed_city = change_city(id)
                return typed_city


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                 
        received_mes = event.message.lower()
        
        id = event.user_id
        name = get_name(id)
        
        if received_mes == "начать":
            city = get_city(id)
            if city != None:
                send_message(id, f'Добро пожаловать, {name}', keyboards.start.get_empty_keyboard())
                send_message(id, f'Ваш город {city.capitalize()}?', keyboards.keyboard_city_aprove)
                city = yes_or_no(id,city)
                
            else:
                send_message(id, f'Добро пожаловать, {name}\nВведите ваш город:')
                city = change_city(id)           
        
        elif received_mes == 'изменить город':
            send_message(id, 'Введите ваш город', keyboards.start.get_empty_keyboard())
            city = change_city(id)

        elif received_mes == 'погода':
            send_message(id, 'Выберите:', keyboards.weather)

        elif received_mes == 'погода на сегодня':
            send_message(id, get_weather_today(city), keyboards.main_menu)
        
        elif received_mes == 'погода на завтра':
            send_message(id, get_weather_tomorrow(city), keyboards.main_menu)

        elif received_mes == 'пробка':
            send_message(id, get_traffic(city), keyboards.main_menu)
        
        elif received_mes == 'валюта':
            send_message(id, get_currency(), keyboards.main_menu)

        elif received_mes == 'афиша':
            send_message(id, 'Выберите:', keyboards.afisha)

        elif received_mes == 'афиша на сегодня':
            send_message(id, get_afisha_main(city, 1), keyboards.main_menu)
        
        elif received_mes == 'афиша на завтра':
            send_message(id, get_afisha_main(city, 2), keyboards.main_menu)    
        
                                    
        else:
            send_message(id, 'Введите допустимую команду', keyboards.start)




