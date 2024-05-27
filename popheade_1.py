import requests
from bs4 import BeautifulSoup


def head():
    url='https://play.google.com/store/apps/details?id=tw.txwy.and.arknights'

    header={
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            }

    data=requests.get(url)
    data.encoding='utf-8'
    data=data.text

    soup=BeautifulSoup(data,'html.parser')
    t1=soup.find('div',class_='PyyLUd')
    t2=t1.find('video')
    t3=t2.find('source').get('src')

    return t3


print(head())