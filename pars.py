from types import NoneType
import requests
from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup
from IPython.display import Image, display
import pandas as pd
from tqdm import tqdm
import time
import json

url2 = 'https://www.litres.ru/popular/?page=1'


#page = requests.get(url2)

#soup = BeautifulSoup(page.text, 'html.parser')
#news_items = soup.find_all(class_='ArtV2Default_wrapper__ENxvA ArtV2Default_wrapper__adaptive__2tegx ArtV2Default_v4__bVeTN')


url = 'https://kenwood.ru/shop'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
news_items = soup.find_all(class_='shop-cart')
c = 0



for i in range(1, 4):
    print(i)
    url_km = 'https://kenwood.ru/category/kuhonnye-mashiny/' + str(i)
    response_km = requests.get(url_km).text
    soup_km = BeautifulSoup(response_km, 'html.parser')
    km_items = soup_km.find_all(class_='product-card--shop')

    for item in km_items:

        if item.find(class_='card-item__display-title') != None:

            img = item.find(class_='card-item__img')
            image_tag = img.find('img')
            image = image_tag['src']
            display(Image(url=image)) #выводим картинку


            title_km = item.find(class_='card-item__display-title').text
            full_title_km = item.find(class_='card-item__title').text
            print('Наименование: ' + title_km.strip() + '\n' +
            'Полное наименование: ' + full_title_km.strip())

            if item.find(class_='prev') != None:
                full_cost_km = item.find(class_='prev').text
                print('Полная стоимость:' + full_cost_km.strip())
                lower_price_km = item.find(class_='curr').text
                print('Сниженная стоимость:' + lower_price_km.strip())

            else: 
                cost_km = item.find(class_='curr').text
                print('Полная стоимость:' + cost_km.strip())

            if item.find(class_='label label-orange') != None:
                additional_km = item.find(class_='label label-orange').text
                if additional_km == 'Хит продаж':
                    print(additional_km)
                elif additional_km == 'New':
                    print('Новинка')
            else:
                pass

            if item.find(class_='label label-orange label-gift') != None: print('При покупке предусмотрен подарок')
            else:
                pass
                

            if item.find(class_='label label-purple') != None:
                percent_km = item.find(class_='label label-purple').text
                if percent_km == 'Предзаказ':
                    print('Только по предзаказу')
                else: 
                    print('Cкидка' + percent_km)

            if item.find(class_='not-available') != None:
                not_available_km = item.find(class_='not-available').text
                if not_available_km == 'Нет в наличии':
                    print(not_available_km + '\n')
            else:
                print('В наличии' + '\n')
        else:
            pass

        