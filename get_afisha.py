import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

month_dict = {
    "Январь": 1,
    "Февраль": 2,
    "Март": 3,
    "Апрель": 4,
    "Май": 5,
    "Июнь": 6,
    "Июль": 7,
    "Август": 8,
    "Сентябрь": 9,
    "Октябрь": 10,
    "Ноябрь": 11,
    "Декабрь": 12
}

def get_afisha_main(city, d_count):
    with open('cities.json', 'r', encoding='utf-8-sig') as f:
        cities = json.load(f)
        city = city.capitalize()
        if city in cities:
            new_city = cities.get(city)
            events = is_there_any_events_in_next_two_days(new_city)
            if events:
                return events
            else:
                if d_count == 1:
                    list_of_shows = afisha_today(new_city)
                    return list_of_shows
                else:
                    list_of_shows = afisha_tomorrow(new_city)
                    return list_of_shows         
        else:
            return 'Вашего города нет в Афише'



def is_there_any_events_in_next_two_days(city):

    url = f'https://www.afisha.ru/{city}/events/na-zavtra/performances/exhibitions/concerts/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    month = soup.find('div', class_='SHPr1').text
    day = soup.find('span', class_='IM0ac').text
    month_number = month_dict.get(month)
    month_number_padded = str(month_number).zfill(2)
    day_padded = str(day).zfill(2)
    date_to_check = day_padded + '.' + month_number_padded
    day_minus_1 = int(day) + 1
    day_minus_1 = str(day_minus_1).zfill(2)
    day_minus_1 = day_minus_1 + '.' + month_number_padded

    today = datetime.today()
    date_today = today.strftime("%d.%m")

    if date_to_check != date_today and date_to_check != day_minus_1:
        return 'В ближайшие два дня в вашем городе нет событий в Афише'



def afisha_today(city):
    url_today = f'https://www.afisha.ru/{city}/events/na-segodnya/'
    headers = { 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

    r = requests.get(url_today, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    names = soup.find_all('div', class_='mQ7Bh')[:5]
    hrefs = soup.find_all('a', class_='vcSoT dcsqk atqQM')[:5]
    prices = soup.find_all('span', class_='Ef2IR jEnBm MDhmt ouqW6')[:5]
    return_message = ''
    lenght = len(prices)
    for i in range(lenght):

        if prices[i].text != 'Билеты':
            price = f'- Билеты {prices[i].text.lower()}'
        else:
            try:
                href = f"https://www.afisha.ru{hrefs[i].get('href')}"
                r = requests.get(href)
                soup = BeautifulSoup(r.content, 'lxml')
                price = '- Билеты ' + soup.find('div', class_='v3nRD zMh5f').text.lower()
            except AttributeError:
                price = '- Билетов нет в продаже'

        return_message += (f"{names[i].text} {price}\nhttps://www.afisha.ru{hrefs[i].get('href')}\n")
    return return_message

def afisha_tomorrow(city):
    url_tomorrow = f'https://www.afisha.ru/{city}/events/na-zavtra/'
    headers = { 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

    r = requests.get(url_tomorrow, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    names = soup.find_all('div', class_='mQ7Bh')[:5]
    hrefs = soup.find_all('a', class_='vcSoT dcsqk atqQM')[:5]
    prices = soup.find_all('span', class_='Ef2IR jEnBm MDhmt ouqW6')[:5]
    return_message = ''
    lenght = len(prices)
    for i in range(lenght):
        if prices[i].text != 'Билеты':
            price = f'- Билеты {prices[i].text.lower()}'
        else:
            try:
                href = f"https://www.afisha.ru{hrefs[i].get('href')}"
                r = requests.get(href)
                soup = BeautifulSoup(r.content, 'lxml')
                price = '- Билеты ' + soup.find('div', class_='v3nRD zMh5f').text.lower()
            except AttributeError:
                price = '- Билетов нет в продаже'
            

        return_message += (f"{names[i].text} - {price}\nhttps://www.afisha.ru{hrefs[i].get('href')}\n")
    return return_message
   

