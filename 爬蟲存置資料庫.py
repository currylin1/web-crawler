
import requests
from bs4 import BeautifulSoup
import db


url='https://forum.gamer.com.tw/B.php?page=1&bsn=33651'

header={
        'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
'Cookie':
'nologinuser=019c86406d93e0634fc8a12c4da2b64b7f41327fc342034b65326f903126; ckM=2095055395; _ga_MT7EZECMKQ=GS1.1.1697811109.2.0.1697811109.60.0.0; ckFORUM_bsn=33651; ckBahaAd=----------------0--------; ckBH_lastBoard=[[%2233651%22%2C%22%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%22]]; buap_modr=p019; buap_puoo=p402%20p401%20p101; _gid=GA1.3.589502488.1699153111; __cf_bm=UHpr8Sa3aaouRPy47Zu3PXvO_a81gJ3qY1J77O2qpY8-1699155343-0-AbOo8N6/oBXf3OxAo4Hp1eHxrq4O8kysYurB/t2D2JPBgqyEDp9dvRm2nxB/8c4Cy2LOsL7mgFEyjp0enww5NhA=; __gads=ID=228c2c6d187cc2fb:T=1693668630:RT=1699155710:S=ALNI_MYgK_5KQEHtIEC6kSzxdISJFfNrIg; __gpi=UID=00000c39c31eb778:T=1693668630:RT=1699155710:S=ALNI_MZnJA16hABoHOS7O8kSTGDQigjdQg; _ga=GA1.1.588056014.1693668626; _ga_2Q21791Y9D=GS1.1.1699153131.5.1.1699155858.60.0.0'
        }

x=50
y=1
for a1 in range(y,x):
    url='https://forum.gamer.com.tw/B.php?page='+str(a1)+'&bsn=33651'    
    data=requests.get(url,headers=header).text
    soup=BeautifulSoup(data,'html.parser')
    title=soup.find_all('div',class_='b-list__tile')  
    print('a1=',a1) 
    for t in title:
        try:
            
            tt=t.find('p').text
            link='https://forum.gamer.com.tw/'+t.find('p').get('href')
            # print(link)
            # print(tt)
            
            # print('-'*100)
            if '繪圖' in tt:
                url2=link
                data=requests.get(url2,headers=header).text
                soup=BeautifulSoup(data,'html.parser')
                title=soup.find('div',class_='c-post__body')

                photo=title.find('img').get('data-src')
                title1=soup.find('h1').text
                print('標題',title1)
                print('繪圖 : ',photo)
                content3=soup.find('div',class_='c-article__content').text
                print('文字內容:',content3)
                date=soup.find('div',class_='c-post__header__info')
                date=date.find('a').get('data-mtime')
                date=date[0:11]
                print(date)  

                sql="insert into games(title,title_photo,content_text,class_,game_name,date_time,link_url) values('{}','{}','{}','繪圖','明日方舟','{}','{}')".format(title1,photo,content3,date,link)
                db.cursor.execute(sql)
                db.conn.commit()      
            if '情報' in tt:
                url2=link
                data=requests.get(url2,headers=header).text
                soup=BeautifulSoup(data,'html.parser')
                title_photo=soup.find('a',class_='photoswipe-image')
                title_photo2=title_photo.get('href')            
                
                title=soup.find('h1').text
                
                content=soup.find('div',class_='c-article__content')
                content1=content.find_all('div')[1]
                content2=content1.find('a').get('href')
                
   
                print('標題圖片:',title_photo2)
                print('標題:',title)
                print('內容連結:',content2)
                
                content3=soup.find('div',class_='c-article__content').text
                print('文字內容:',content3)
                
                date=soup.find('div',class_='c-post__header__info')
                date=date.find('a').get('data-mtime')
                date=date[0:11]
                print(date)
   #-------------------------------------------------------------------------------------------------------------------------------------------------------------------


                sql="insert into games(title,title_photo,content_text,class_,game_name,date_time,link_url) values('{}','{}','{}','情報','明日方舟','{}','{}')".format(title,title_photo2,content3,date,link)
                db.cursor.execute(sql)
                db.conn.commit()
                
            if '閒聊' in tt:
                url2=link
                data=requests.get(url2,headers=header).text
                soup=BeautifulSoup(data,'html.parser')
                title_photo=soup.find('a',class_='photoswipe-image')
                title_photo2=title_photo.get('href')            
                
                title=soup.find('h1').text
                
                content=soup.find('div',class_='c-article__content')
                # content1=content.find_all('div')[1]
                # content2=content1.find('a').get('href')
                content3=soup.find('div',class_='c-article__content').text
                

                print('標題圖片:',title_photo2)
                print('標題:',title)
                # print('內容連結:',content2)
                print('文字內容:',content3)
                
                
                date=soup.find('div',class_='c-post__header__info')
                date=date.find('a').get('data-mtime')
                date=date[0:11]
                print(date)
                sql="insert into games(title,title_photo,content_text,class_,game_name,date_time,link_url) values('{}','{}','{}','閒聊','明日方舟','{}','{}')".format(title,title_photo2,content3,date,link)
                db.cursor.execute(sql)
                db.conn.commit()
            if '討論' in tt:
                url2=link
                data=requests.get(url2,headers=header).text
                soup=BeautifulSoup(data,'html.parser')
                title_photo=soup.find('a',class_='photoswipe-image')
                title_photo2=title_photo.get('href')            
                
                title=soup.find('h1').text
                
                content=soup.find('div',class_='c-article__content')
                # content1=content.find_all('div')[1]
                # content2=content1.find('a').get('href')
                content3=soup.find('div',class_='c-article__content').text
                
                print('標題:',title)  
                print('標題圖片:',title_photo2)
                print('文字內容:',content3)   
                
                date=soup.find('div',class_='c-post__header__info')
                date=date.find('a').get('data-mtime')
                date=date[0:11]
                print(date)
                sql="insert into games(title,title_photo,content_text,class_,game_name,date_time,link_url) values('{}','{}','{}','討論','明日方舟','{}','{}')".format(title,title_photo2,content3,date,link)
                db.cursor.execute(sql)
                db.conn.commit()


        except AttributeError:
            print('erro')
        except NameError:
            print('erro')
        except IndexError:
            print('erro')

        

    
db.conn.close()
