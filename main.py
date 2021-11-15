# Спринт №2,разработчик - Горлинский К.О., вывод новостей из группы в вк
import requests  # Url 
from bs4 import BeautifulSoup  # Html
from token import token

OMSTUNEWS = "https://www.vk.com/omskpoliteh"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"} # Я ЛИЧНОСТЬ!!! Х)

UniNews = requests.get(OMSTUNEWS, headers=headers)  # лямзим разметку с сайта)
Omsknewssoup = BeautifulSoup(UniNews.content, 'html.parser')
OMNEW = Omsknewssoup.find_all("span", {class="_post post page_block all own post--withPostBottomAction  post--with-likes deep_active"})
    print(OMNEW) # выводим пост
    for post in posts: # вывод постов с картинками в макс. разрешении
         post = post["id"]
        try:
            if "attachments" in posts:
                post = post["attachments"]

                if post[0]["type"] == "photo":

                    photo_qual = [
                        "photo_2560",
                        "photo_1280",
                        "photo_807",
                        "photo_640",
                        "photo_130",
                        "photo_75",
                    ]

                    if len(post) == 1:  # для постов с несколькими картинками

                        for pq in photo_qual:
                            post_photo = post[0]["photo"][pq]
                            print(post_photo)
                            break
                    else:
                        for post_item_photo in post:
                            if post_item_photo ["type"] == "photo":
                                for pq in photo_qual:
                                    if pq in post_item_photo["photo"]:
                                        post_photo = post_item_photo["photo"][pq]
                                        print(post_photo)
                                        break
