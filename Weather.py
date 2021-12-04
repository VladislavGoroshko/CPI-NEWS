# Спринт №2, разработчик - Зубович Н.В., вывод погоды.
import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup  # Модуль для работы с HTML
import time  # Модуль для остановки программы

WeatherOmsk='https://www.gismeteo.ru/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

OmWeatherFullPage = requests.get(WeatherOmsk, headers=headers)  # Вывод полной разметки HTML страницы
OmWeathersoup = BeautifulSoup(OmWeatherFullPage.content, 'html.parser')

OmWeather=OmWeathersoup.find_all('span', {'value unit unit_temperature_c'})
OmWeatherInfo=OmWeathersoup.find_all('div', {'description gray'})
WeatherInfo = str(OmWeatherInfo)[str(OmWeatherInfo).find('М'): str(OmWeatherInfo).rfind('<')]
x = str(OmWeather[0]).split()[4][:str(OmWeather[0]).split()[4].rfind('<span')]
y = str(OmWeather[0]).split()[5][str(OmWeather[0]).split()[5].find(">")+1:str(OmWeather[0]).split()[5].rfind("</")]
#print('Сейчас в Омске',WeatherInfo.lower())
print('Температура в Омске на данный момент времени:', x+y ,'градусов по Цельсию')