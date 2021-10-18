import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
DOLLAR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83&aqs=chrome.0.69i59j69i57j69i59j35i39j0i20i263i433i512j69i61l3.2421j1j7&sourceid=chrome&ie=UTF-8'
EURO_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sxsrf=AOaemvL7Qmv2CovVFmXCEtty_xADOR2lAg%3A1634560629608&ei=dWptYYzQJO-Oxc8PxMuiCA&ved=0ahUKEwjM3sPt_NPzAhVvR_EDHcSlCAEQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEEYQggIyBQgAEIAEMgUIABCABDIICAAQgAQQsQMyCAgAEIAEELEDMgsIABCABBCxAxCDATIICAAQgAQQyQMyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQM6BwgjELADECc6BwgAEEcQsAM6BwgAELADEEM6BwgAELEDEAo6BwgAEIAEEAo6BAgjECc6EAgAEIAEEIcCELEDEIMBEBRKBAhBGABQwOw6WK3_OmC_gTtoAXACeACAAZEBiAHFB5IBAzAuN5gBAKABAcgBCsABAQ&sclient=gws-wiz'
DOLLARheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
UEROheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.686 Yowser/2.5 Safari/537.36'}

DOLLARfull_page = requests.get(DOLLAR_RUB, Dollarheaders=Dollarheaders) #Вывод полной разметки HTML страницы
EUROfull_page = requests.get(DOLLAR_RUB, EUROheaders=EUROheaders)



DOLLARsoup = BeautifulSoup(DOLLARfull_page.content, 'html.parser')
EUROsoup = BeautifulSoup(EUROfull_page.content, 'html.parser')


DOLLARconvert = DOLLARsoup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision":2})

EUROconvert = EUROsoup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision":2})
print("Курс одного доллара =" + " " + DOLLARconvert[0].text + " " + "рублей")






