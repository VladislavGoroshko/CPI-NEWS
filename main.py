import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
DOLLAR_RUB = 'https://www.cbr.ru/currency_base/daily/' #Ссылка на сайт центробанка РФ где указаны все курсы валют
EURO_RUB = 'https://www.cbr.ru/currency_base/daily/' #Ссылка на сайт центробанка РФ где указаны все курсы валют
TENGE_RUB = 'https://www.cbr.ru/currency_base/daily/' #Ссылка на сайт центробанка РФ где указаны все курсы валют
STERLING_RUB = 'https://www.cbr.ru/currency_base/daily/' #Ссылка на сайт центробанка РФ где указаны все курсы валют
GRIVEN_RUB = 'https://www.cbr.ru/currency_base/daily/' #Ссылка на сайт центробанка РФ где указаны все курсы валют
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'} #Заголовки для передачи вместе с URL
Dollarfull_page = requests.get(DOLLAR_RUB, headers=headers) #Вывод полной разметки HTML страницы доллара
Eurofull_page = requests.get(EURO_RUB, headers=headers) #Вывод полной разметки HTML страницы евро
Tengefull_page = requests.get(TENGE_RUB,headers=headers) #Вывод полной разметки HTML страницы тенге
Sterlingfull_page = requests.get(STERLING_RUB,headers=headers) #Вывод полной разметки HTML страницы фунтов стерлинга
Grivenfull_page = requests.get(GRIVEN_RUB, headers=headers) #Вывод полной разметки HTML страницы гривен



Dollarsoup = BeautifulSoup(Dollarfull_page.content, 'html.parser') #Парсим страницу через библиотеку BeautifuelSoup
Eurosoup = BeautifulSoup(Eurofull_page.content, 'html.parser') #Парсим страницу через библиотеку BeautifuelSoup
Tengesoup = BeautifulSoup(Tengefull_page.content, 'html.parser') #Парсим страницу через библиотеку BeautifuelSoup
Sterlingsoup= BeautifulSoup(Sterlingfull_page.content, 'html.parser') #Парсим страницу через библиотеку BeautifuelSoup
Grivensoup = BeautifulSoup(Grivenfull_page.content, 'html.parser') #Парсим страницу через библиотеку BeautifuelSoup

Grivenconvert = Grivensoup.find_all("tr") #Находим нужный для нас html тэг на сайте центробанка этот тег "tr"
Sterlingconvert = Sterlingsoup.find_all("tr") #Находим нужный для нас html тэг на сайте центробанка этот тег "tr"
Tengeconvert = Tengesoup.find_all("tr") #Находим нужный для нас html тэг на сайте центробанка этот тег "tr"
Euroconvert = Eurosoup.find_all("tr") #Находим нужный для нас html тэг на сайте центробанка этот тег "tr"
Dollarconvert = Dollarsoup.find_all("tr") #Находим нужный для нас html тэг на сайте центробанка этот тег "tr"
a=str(Dollarconvert[11]).split() # Разбиваем строку на элементы
b=str(a[6]) # Выбираем 6 элемент строки
t=b[4:11] # Делаем срез (остаются символы с 4 по 11)
a1=str(Euroconvert[12]).split() # Разбиваем строку на элементы
b1=str(a1[5]) # Выбираем 5 элемент строки
t1=b1[4:11] # Делаем срез (остаются символы с 4 по 11)
a2=str(Tengeconvert[14]).split() # Разбиваем строку на элементы
b2=str(a2[6]) # Выбираем 6 элемент строки
t2=b2[4:11] # Делаем срез (остаются символы с 4 по 11)
a3=str(Sterlingconvert[29]).split() # Разбиваем строку на элементы
b3=str(a3[8]) # Выбираем 8 элемент строки
t3=b3[4:11] # Делаем срез (остаются символы с 4 по 11)
a4=str(Grivenconvert[28]).split() # Разбиваем строку на элементы
b4=str(a4[6]) # Выбираем 6 элемент строки
t4=b4[4:11] # Делаем срез (остаются символы с 4 по 11)
print("Курс одного доллара =" + " " + t + " " + "рублей") #Вывод курса валюты на экран
print("Курс одного евро =" + " " + t1 + " " + "рублей") #Вывод курса валюты на экран
print("Курс ста теньге =" + " " + t2 + " " + "рублей") #Вывод курса валюты на экран
print("Курс одного фунта стерлингов =" + " " + t3 + " " + "рублей") #Вывод курса валюты на экран
print("Курс десяти украинских гривен =" + " " + t4 + " " + "рублей") #Вывод курса валюты на экран




