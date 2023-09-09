import requests
from bs4 import BeautifulSoup


def get_currency():
    url = 'https://www.cbr.ru/currency_base/daily/'        
    headers = { 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    rub_to_usd = soup.find('td', string='Доллар США').next_element.next_element.next_element.text
    rub_to_eur = soup.find('td', string='Евро').next_element.next_element.next_element.text
    rub_to_gbp = soup.find('td', string='Фунт стерлингов Соединенного королевства').next_element.next_element.next_element.text
    rub_to_cny = soup.find('td', string='Китайский юань').next_element.next_element.next_element.text
    rub_to_aud = soup.find('td', string='Австралийский доллар').next_element.next_element.next_element.text

    return f'Доллар США (USD) - {rub_to_usd[:-2]}₽\nЕвро (EUR) - {rub_to_eur[:-2]}₽\nБританский фунт стерлингов (GBP) - {rub_to_gbp[:-2]}₽\nКитайский юань (CNY) - {rub_to_cny[:-2]}₽\nАвстралийский доллар (AUD) - {rub_to_aud[:-2]}₽'



