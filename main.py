import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
DOLLAR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83&aqs=chrome.0.69i59j69i57j69i59j35i39j0i20i263i433i512j69i61l3.2421j1j7&sourceid=chrome&ie=UTF-8'
EURO_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&aqs=chrome.0.69i59j35i39j0i20i263i512l2j0i433i512j69i61j69i60l2.1957j0j9&sourceid=chrome&ie=UTF-8'
headers_dollar = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
headers_euro = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
DOLLARfull_page = requests.get(DOLLAR_RUB, headers_dollar=headers_dollar) #Вывод полной разметки HTML страницы
EUROfull_page = requests.get(EURO_RUB, headers_euro=headers_euro)



DOLLARsoup = BeautifulSoup(DOLLARfull_page.content, 'html.parser')
EUROsoup= BeautifulSoup(EUROfull_page.content), 'html.parser'


DOLLARconvert = DOLLARsoup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision":2})
EUROconvert = EUROsoup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision":2})

print("Курс одного доллара =" + " " + DOLLARconvert[0].text + " " + "рублей")
print("Курс одного евро =" + " " + DOLLARconvert[0].text + " " + "рублей")






