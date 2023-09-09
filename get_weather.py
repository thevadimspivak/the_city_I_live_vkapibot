import requests
from datetime import date, timedelta
from mytoken import api


d = date.today()
tomorrow = d + timedelta(days=1)
morning = str(d) + ' 06:00:00'
day = str(d) + ' 12:00:00'
evening = str(d) + ' 21:00:00'
morning_t = str(tomorrow) + ' 06:00:00'
day_t = str(tomorrow) + ' 12:00:00'
evening_t = str(tomorrow) + ' 21:00:00'

smiles = {
    'пасмурно': '&#9729;',
    'ясно': '&#9728;',
    'небольшой дождь': '&#127783;',
    'переменная облачность': '&#9925;',
    'пасмурно': '&#9729;',
    'небольшой снег': '&#127784;',
    'снег': '&#10052;',
    'облачно с прояснениями': '&#127781;'

}


def get_weather_today(city):
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={api}'
        response = requests.get(url).json()
        cord = response.get('coord')
        lat = cord.get('lat')
        lon = cord.get('lon')

        url2 = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api}&lang=ru&units=metric&cnt=13'
        big_response = requests.get(url2).json()
        big_response = big_response.get('list')
    except AttributeError:
        error_message = 'Введите существующее название города'
        return error_message
    
    weather_message = 'Температура сегодня:\n'
    for dt in big_response:
        if dt['dt_txt'] == morning:
            temp = round(dt['main']['temp'])
            humidity = dt['main']['humidity']
            description = dt['weather'][0]['description']
            smile = smiles.get(description, '&#127774;')
            weather_morning = f'{smile} Утро {temp}°C, {description}, влажность {humidity}%'
            weather_message += str(weather_morning) + '\n'

        elif dt['dt_txt'] == day:
            temp = round(dt['main']['temp'])
            humidity = dt['main']['humidity']
            description = dt['weather'][0]['description']
            smile = smiles.get(description, '&#127774;')
            weather_day = f'{smile} Днём {temp}°C, {description}, влажность {humidity}%'
            weather_message += str(weather_day) + '\n'
            
        elif dt['dt_txt'] == evening:
            temp = round(dt['main']['temp'])
            humidity = dt['main']['humidity']
            description = dt['weather'][0]['description']
            smile = smiles.get(description, '&#127774;')
            weather_evening = f'{smile} Вечер {temp}°C, {description}, влажность {humidity}%'
            weather_message += str(weather_evening)
           
    return weather_message
    
   
def get_weather_tomorrow(city):
    try: 
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={api}'
        response = requests.get(url).json()
        cord = response.get('coord')
        lat = cord.get('lat')
        lon = cord.get('lon')

        url2 = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api}&lang=ru&units=metric&cnt=13'
        big_response = requests.get(url2).json()
        big_response = big_response.get('list')
    except AttributeError:
        error_message = 'Введите существующее название города'
        return error_message
    
    weather_message = 'Температура завтра:\n'
    for dt in big_response:
        if dt['dt_txt'] == morning_t:
            temp = round(dt['main']['temp'])
            humidity = dt['main']['humidity']
            description = dt['weather'][0]['description']
            smile = smiles.get(description, '&#127774;')
            weather_morning = f'{smile} Утро {temp}°C, {description}, влажность {humidity}%'
            weather_message += str(weather_morning) + '\n'

        elif dt['dt_txt'] == day_t:
            temp = round(dt['main']['temp'])
            humidity = dt['main']['humidity']
            description = dt['weather'][0]['description']
            smile = smiles.get(description, '&#127774;')
            weather_day = f'{smile} Днём {temp}°C, {description}, влажность {humidity}%'
            weather_message += str(weather_day) + '\n'
            
        elif dt['dt_txt'] == evening_t:
            temp = round(dt['main']['temp'])
            humidity = dt['main']['humidity']
            description = dt['weather'][0]['description']
            smile = smiles.get(description, '&#127774;')
            weather_evening = f'{smile} Вечер {temp}°C, {description}, влажность {humidity}%'
            weather_message += str(weather_evening)
           
    return weather_message
    