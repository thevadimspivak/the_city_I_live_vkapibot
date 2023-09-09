
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from mytoken import api
import requests
import json


def get_traffic(city):
    try:    
        headers = {
            'user_agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'Accept': '*/*'
        }

        options = Options()
        # options.add_argument("--headless")
        # options.add_argument('--incognito')
        options.add_argument(f'--user-agent={headers}')

        s = Service(executable_path="D:\dev\Chrome_webdriver\chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=options)

        
        headers2 = { 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={api}'
        response = requests.get(url, headers=headers2).json()
        cord = response.get('coord')
        lon = cord.get('lon')
        lat = cord.get('lat')

        url2 = f'https://yandex.ru/maps/probki/?ll={lon}%2C{lat}&z=11'
        driver.get(url2)
        sleep(3)
        traffic = driver.find_element(By.CLASS_NAME, 'traffic-panel-view__dropdown-title').text
        
        if traffic == 'Пробки':
            return 'Нет данных для этого города.'
        else:
            return traffic
    except NoSuchElementException:
        return 'Нет данных для этого города.'
    
