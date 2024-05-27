from flask import Flask,render_template,request,redirect,url_for
import db
from flask_paginate import Pagination,get_page_parameter  # 做分頁
from datetime import datetime

from popheade_1 import head


app = Flask(__name__)

@app.route('/')
def index():
    he=[head()]

    return render_template('index.html',**locals())

@app.route('/photo')
def photo():

    page = int(request.args.get('page',1))
    sql = "select count(*) as c from game where class_='繪圖'"

    db.cursor.execute(sql)
    datacount = db.cursor.fetchone()
    count = int(datacount[0])   #算總筆數
    p= request.args.get('p','')

    if page == 1 and len(p)==0:
        sql = "select title,title_photo,content_text,class_,game_name,date_time,link_url from game where class_='繪圖' limit 16"
    else:
        startp = page - 1
        sql = "select title,title_photo,content_text,class_,game_name,date_time,link_url from game where class_='繪圖' limit {},{}".format(startp*16,16)


#------------------------------------------------------------------------------------------------------------------------

    if len(p) > 0 :
        sql = "select title,title_photo,content_text,class_,game_name,date_time,link_url from game where class_='繪圖' and title like '%{}%' limit 16".format(p)

    db.cursor.execute(sql)
    result = db.cursor.fetchall()
    pagination=Pagination(page=page,total=count,per_page=16)

    return render_template('photo.html',**locals())

@app.route('/discuss')
def discuss():
    page = int(request.args.get('page',1))
    sql = "select count(*) as c from games where class_='討論'"

    db.cursor.execute(sql)
    datacount = db.cursor.fetchone()
    count = int(datacount[0])   #算總筆數

    if page == 1:
        sql = "select title,title_photo,content_text,class_,game_name,date_time,link_url from game where class_='討論' order by date_time limit 16"
    else:
        startp = page - 1
        sql = "select title,title_photo,content_text,class_,game_name,date_time,link_url from game where class_='討論' limit {},{}".format(startp*16,16)
    db.cursor.execute(sql)
    result = db.cursor.fetchall()
    pagination=Pagination(page=page,total=count,per_page=16)
    return render_template('discuss.html',**locals())


@app.route('/intelligence')
def intelligence():
    page = int(request.args.get('page',1))
    sql = "select count(*) as c from games where class_='情報'"

    db.cursor.execute(sql)
    datacount = db.cursor.fetchone()
    count = int(datacount[0])   #算總筆數

    if page == 1:
        sql = "select title,title_photo,content_text,class_,game_name,date_time,link_url from game where class_='情報' order by date_time limit 16"
    else:
        startp = page - 1
        sql = "select title,title_photo,content_text,class_,game_name,date_time,link_url from game where class_='情報' limit {},{}".format(startp*16,16)
    db.cursor.execute(sql)
    result = db.cursor.fetchall()
    pagination=Pagination(page=page,total=count,per_page=16)
    return render_template('intelligence.html',**locals())


@app.route('/chitchatting')
def chitchatting():
    page = int(request.args.get('page',1))
    sql = "select count(*) as c from games where class_='閒聊'"

    db.cursor.execute(sql)
    datacount = db.cursor.fetchone()
    count = int(datacount[0])   #算總筆數

    if page == 1:
        sql = "select title,title_photo,content_text,class_,game_name,date_time,link_url from game where class_='閒聊' order by date_time limit 16"
    else:
        startp = page - 1
        sql = "select title,title_photo,content_text,class_,game_name,date_time,link_url from game where class_='閒聊' limit {},{}".format(startp*16,16)
    db.cursor.execute(sql)
    result = db.cursor.fetchall()
    pagination=Pagination(page=page,total=count,per_page=16)
    return render_template('chitchatting.html',**locals())

@app.route('/contact')
def message():
    return render_template("contact.html")

@app.route("/opinion",methods=['POST'])
def opinion():
    if request.method == 'POST':
        username = request.form.get('name','')
        title = request.form.get('title')
        content = request.form.get('content')
        today = datetime.today()
        c_date = datetime.strftime(today, '%Y-%m-%d')

        sql = "insert into opinion(subject,name,content,create_date) values('{}','{}','{}','{}')".format(title,username,content,c_date)

        db.cursor.execute(sql)
        db.conn.commit()

    return redirect(url_for('message'))



if __name__ == '__main__':
    app.run(debug=True)




















