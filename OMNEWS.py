import requests

VK_CONFIG = {
    "domain": "https://api.vk.com/method",
    "access_token": "d83d177784092704bd0e22d3cfc18ec180d376a8a30dc0d158b6bb7b5259d78562b8d0145585788c716e0",
    "version": "5.131",
}

domain = VK_CONFIG["domain"]
access_token = VK_CONFIG["access_token"]
v = VK_CONFIG["version"]
ss = -71122446
zapros = f'{domain}/wall.get?access_token={access_token}&owner_id={ss}&count=2&v={v}'
response = requests.get(zapros)
print(response.json()['response']['items'][1]['text'])
print('Читайте больше новостей в оффициальной группе ОмГТУ: https://vk.com/omskpoliteh')