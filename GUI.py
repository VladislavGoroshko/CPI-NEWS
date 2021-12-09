# импорт необходимых для работы библиотек
from tkinter import *
import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time  # Модуль для остановки программы
from datetime import datetime
import pytz
from PIL import Image, ImageTk
# Получение данных о курсах валют. Автор : Горошко Владислав
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
# Создание интерфейса программы через библиотеку tkinter. Авторы : Зубович Никита, Горошко Владислав
root = Tk() # создаём объект библиотеки tkinter
root.title('CPI-NEWS') # прописываем название программы

canv = Canvas(width=1880, height=570)  # создаём "холст" для интерфейса
canv.place(x=0, y=0) # пишем начальные координаты появления холста
img=Image.open("bg.png") # устанавливаем bg.png как задний фон приложения
bg=ImageTk.PhotoImage(img) # устанавливаем bg.png как задний фон приложения
canv.create_image(0, 0, anchor=NW, image=bg) # устанавливаем bg.png как задний фон приложения

Value_lbl = Label(text='Курсы валют', font="TimesNewRoman 17", bg="RoyalBlue") # создаём заголовок блока с курсами валют

USD_lbl1 = Label(text='$ Курс одного доллара:', font="TimesNewRoman 15", bg="LightSkyBlue") # создаём отдельные строки
USD_ent = Label(text=f'{t}',width=7, justify=CENTER, font="TimesNewRoman 15", bg="LightCyan") # для вывода курса
USD_lbl2 = Label(text='рублей', font="TimesNewRoman 15", bg="LightSkyBlue")                    # каждой валюты

EUR_lbl1 = Label(text='€ Курс одного евро:', font="TimesNewRoman 15", bg="LightSkyBlue")
EUR_ent = Label(text = f'{t1}',width=7, justify=CENTER, font="TimesNewRoman 15", bg="LightCyan")
EUR_lbl2 = Label(text='рублей', font="TimesNewRoman 15", bg="LightSkyBlue")

TEN_lbl1 = Label(text='₸ Курс ста тенге:', font="TimesNewRoman 15", bg="LightSkyBlue")
TEN_ent = Label(text =f'{t2}',width=7, justify=CENTER, font="TimesNewRoman 15", bg="LightCyan")
TEN_lbl2 = Label(text='рублей', font="TimesNewRoman 15", bg="LightSkyBlue")

STER_lbl1 = Label(text='£ Курс одного фунта стерлингов:', font="TimesNewRoman 15", bg="LightSkyBlue")
STER_ent = Label(text=f'{t3}',width=7, justify=CENTER, font="TimesNewRoman 15", bg="LightCyan")
STER_lbl2 = Label(text='рублей', font="TimesNewRoman 15", bg="LightSkyBlue")

GRI_lbl1 = Label(text='₴ Курс десяти украинских гривен:', font="TimesNewRoman 15", bg="LightSkyBlue")
GRI_ent = Label(text = f'{t4}',width=7, justify=CENTER, font="TimesNewRoman 15", bg="LightCyan")
GRI_lbl2 = Label(text='рублей', font="TimesNewRoman 15", bg="LightSkyBlue")

Value_lbl.grid(row=0, column=0, columnspan=3, pady=(5,10)) # размещаем созданные ранее объекты в окне интерфейса используя .grid
USD_lbl1.grid(row=1, column=0, sticky='e')
USD_ent.grid(row=1, column=1)
USD_lbl2.grid(row=1, column=2, sticky='w')
EUR_lbl1.grid(row=2, column=0, sticky='e')
EUR_ent.grid(row=2, column=1)
EUR_lbl2.grid(row=2, column=2, sticky='w')
TEN_lbl1.grid(row=3, column=0, sticky='e')
TEN_ent.grid(row=3, column=1)
TEN_lbl2.grid(row=3, column=2, sticky='w')
STER_lbl1.grid(row=4, column=0, sticky='e')
STER_ent.grid(row=4, column=1)
STER_lbl2.grid(row=4, column=2, sticky='w')
GRI_lbl1.grid(row=5, column=0, sticky='e')
GRI_ent.grid(row=5, column=1)
GRI_lbl2.grid(row=5, column=2, sticky='w')
# Блок погоды. Автор : Зубович Никита
WeatherOmsk='https://www.accuweather.com/ru/ru/omsk/294463/weather-forecast/294463'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

OmWeatherFullPage = requests.get(WeatherOmsk, headers=headers)  # Вывод полной разметки HTML страницы
OmWeathersoup = BeautifulSoup(OmWeatherFullPage.content, 'html.parser')
OmWeatherInfo=OmWeathersoup.find_all('span',{'phrase'})  # ищем информацию о погоде по тегу div со значением description gray
OmWeather=OmWeathersoup.find_all('div', {'temp'}) # ищем информацию о температуре по тегу span со значением value unit unit temp...
OmWeatherSub = OmWeathersoup.find_all('span',{'val_to_sub'}) # ищем информацию о десятых градуса по соответствующеему тегу
#if str(OmWeather[0]).split()[0].find('<')==-1:
 #   x = str(OmWeather[0]).split()[4]  # забираем из набора данных данные о температуре
#else:
#    x = str(OmWeather[0]).split()[4][:str(OmWeather[0]).split()[4].find('<')]
x=str(OmWeather).split()[1][str(OmWeather).split()[1].find('>')+1:str(OmWeather).split()[1].rfind('<')]
z = str(OmWeatherInfo).split()[1][str(OmWeatherInfo).split()[1].find('>')+1:str(OmWeatherInfo).split()[1].rfind('<')].lower() # забираем из набора данных данные о погоде и переводим строку в нижний регистр
Weather_lbl = Label(text='Погода', font="TimesNewRoman 17", bg="RoyalBlue") # создаём заголовок для блока погоды
Temp_lbl1 = Label(text=f'Температура в Омске на данный момент времени: ', font="TimesNewRoman 15", bg="LightSkyBlue", justify = CENTER ) # создаём поле для вывода температуры
Temp_lbl2 = Label(text=f'{x}С.', font='TimesNewRoman 15',bg='LightCyan')
Temp_lbl3 = Label(text=f'В Омске {z}', font="TimesNewRoman 15", bg="LightSkyBlue", justify = CENTER) # создаём поле для вывода краткого описания погоды
Inf_lbl = Label(text= 'В Омске ', font="TimesNewRoman 15", bg = "LightSkyBlue")
Inf_ent = Entry(width=15,justify = CENTER, font="TimesNewRoman 15", bg ="LightCyan")
Inf_ent.insert(END, x)

Weather_lbl.grid(row=7, column=0, columnspan=3, pady=(5,0)) # размещаем созданные ранее объекты в окне приложения
Temp_lbl1.grid(row=8, column=0)
Temp_lbl2.grid(row=8,column=1,sticky = 'w')
Temp_lbl3.grid(row=9, column=0,sticky = 'w')

# Блок Новостей. Автор : Горлинский Константин
VK_CONFIG = { # создаём служебный словарь для дальнейшего взаимодействия с сервисом API VK
    "domain": "https://api.vk.com/method",
    "access_token": "d83d177784092704bd0e22d3cfc18ec180d376a8a30dc0d158b6bb7b5259d78562b8d0145585788c716e0",
    "version": "5.131",
}

domain = VK_CONFIG["domain"]
access_token = VK_CONFIG["access_token"]
v = VK_CONFIG["version"]
ss = -71122446 # задаём ID группы ВК из которой будет браться информация
zapros = f'{domain}/wall.get?access_token={access_token}&owner_id={ss}&count=2&v={v}' # собираем URL-адрес страницы нашего запроса
response = requests.get(zapros) # делаем запрос по ранее собранной ссылке для получения необходимой информации

News_lbl = Label(text='Новости', font="TimesNewRoman 17", bg="RoyalBlue") # создаём заголовок Блока Новостей
News_txt = Text(height=14, width=100, font="TimesNewRoman 15", bg="LightCyan") # создаём поле многострочного текста
scrollbar_nws = Scrollbar(root, command=News_txt.yview) # создаём скролл-бар для поля многострочного текста

News_txt.insert(END, response.json()['response']['items'][1]['text']) # забираем интересующую нас информацию из ответа на сделанный нами запрос и вводим её в созданное ранее текстовое поле.
News_txt.insert(END, '\nЧитайте больше новостей в оффициальной группе ОмГТУ: https://vk.com/omskpoliteh')
News_txt.config(state = DISABLED) # запрещаем редакцию текстового поля

News_lbl.grid(row=6, column=3, pady=(5,10)) # размещаем созданные ранее объекты в окне приложения.
News_txt.grid(row=7, column=3, rowspan=9)
scrollbar_nws.grid(row=7, column=4, rowspan=9, sticky='nws')
News_txt.configure(yscrollcommand=scrollbar_nws.set)
# Блок Времени. Автор : Демиденко Максим
tz_Omsk = pytz.timezone('Asia/Omsk')
datetime_Omsk = datetime.now(tz_Omsk)
#print("Omsk time:", datetime_Omsk.strftime("%H:%M:%S"))

def update_time(): # создаём функцию о
    Time_lbl2.config(text=f"{datetime.now():%H:%M:%S}")
    Time_lbl2.after(100, update_time)

Time_lbl1=Label(text="Время", font="TimesNewRoman 17", bg="RoyalBlue")
Time_lbl2=Label(text=f"{datetime.now():%H:%M:%S}", font="TimesNewRoman 30", bg="LightCyan")
Time_lbl1.grid(row=0, column=3, columnspan=2)
Time_lbl2.grid(row=1, column=3, columnspan=2, rowspan=5)
update_time()

cred_lbl=Label(text='Графический интерфейс разработан:\n Зубович Н.В. Горошко В.И. \n Все права защищены ©', justify=CENTER, font="TimesNewRoman 15", bg="LightCyan")
cred_lbl.grid(row=13,column=0, columnspan=3)

root.mainloop()