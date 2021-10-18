import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
DOLLAR_RUB = 'https://www.cbr.ru/currency_base/daily/'
EURO_RUB = 'https://www.cbr.ru/currency_base/daily/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
Dollarfull_page = requests.get(DOLLAR_RUB, headers=headers) #Вывод полной разметки HTML страницы
Eurofull_page = requests.get(EURO_RUB, headers=headers)



Dollarsoup = BeautifulSoup(Dollarfull_page.content, 'html.parser')
Eurosoup = BeautifulSoup(Eurofull_page.content, 'html.parser')

Euroconvert = Eurosoup.find_all("tr")
Dollarconvert = Dollarsoup.find_all("tr")
a=str(Dollarconvert[11]).split() # Разбиваем строку на элементы
b=str(a[6]) # Выбираем 6 элемент строки
t=b[4:11] # Делаем срез (остаются символы с 4 по 11)
a1=str(Euroconvert[12]).split()
b1=str(a1[5])
t1=b1[4:11]
print("Курс одного доллара =" + " " + t + " " + "рублей")
print("Курс одного евро =" + " " + t1 + " " + "рублей")






