import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
DOLLAR_RUB = 'https://www.cbr.ru/currency_base/daily/'
EURO_RUB = 'https://www.cbr.ru/currency_base/daily/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
Dollarfull_page = requests.get(DOLLAR_RUB, headers=headers) #Вывод полной разметки HTML страницы
Eurofull_page = requests.get(EURO_RUB, headers=headers)



Dollarsoup = BeautifulSoup(Dollarfull_page.content, 'html.parser')



Dollarconvert = Dollarsoup.find_all("tr",{})








