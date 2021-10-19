import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup  # Модуль для работы с HTML
import time  # Модуль для остановки программы

WeatherOmsk='https://www.gismeteo.ru/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

OmWeatherFullPage = requests.get(WeatherOmsk, headers=headers)  # Вывод полной разметки HTML страницы
OmWeathersoup = BeautifulSoup(OmWeatherFullPage.content, 'html.parser')

OmWeather=OmWeathersoup.find_all('span', {'value unit unit_temperature_c'})
x=str(OmWeather[0])
x1=x.split()
y=str(x1[4])
if y[3]!='<':
    yred=y[:2]
else:
    yred=y[:3]
z=str(x1[5])
zred=z[19:21]
print('Температура в Омске на данный момент времени:', yred+zred,'градусов по Цельсию')