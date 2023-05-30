import os
from datetime import datetime
from flask import Blueprint, render_template, url_for, request,g,flash
from werkzeug.utils import redirect,secure_filename

from pybo.models import News,NewsImg
from pybo import db

from pybo.utils import save_image,delete_image
from pybo.views.auth_views import login_required

bp = Blueprint('news',__name__,url_prefix='')

@bp.route('/News')
def NewsDef():
    newsList = News.query.order_by(News.activity_date.desc()).all()
    return render_template('News/news.html',newsList=newsList)


@bp.route('/News/create', methods=['GET','POST'])
@login_required
def create_news():
    if request.method == 'POST':
        activity_date = request.form['activity_date']
        activity = request.form['activity']
        content = request.form['content']
        images = request.files.getlist('images[]')
        create_date = datetime.now()
        new_news = News(activity_date=activity_date,activity=activity,content=content,create_date=create_date)

        for image in images:
            image_path = save_image(image,'news')
            news_img = NewsImg(image_path=image_path,folder='news')
            new_news.images.append(news_img)
            
        db.session.add(new_news)
        db.session.commit()
        
        return redirect(url_for('news.NewsDef'))
    else:
        return render_template('News/create_news.html')

'''
@bp.route('/News/modify/<int:news_id>',methods=('GET','POST'))
@login_required
def modify(news_id):
    news = News.query.get_or_404(news_id)
    if request.method == 'POST':
        news.modify_date=datetime.now()
        db.session.commit()
        return redirect(url_for('news.NewsDef'))
    else: # GET 요청
    return render_template('News/create_news.html')
'''

@bp.route('/News/modify/<int:news_id>', methods=('GET', 'POST'))
@login_required
def modify(news_id):
    news = News.query.get_or_404(news_id)

    if request.method == 'POST':
        activity_date = request.form['activity_date']
        activity = request.form['activity']
        content = request.form['content']
        images = request.files.getlist('images[]')

        news.activity_date = activity_date
        news.activity = activity
        news.content = content

        # 기존 이미지 삭제
        for image in news.images:
            delete_image(image.folder, image.image_path)
            db.session.delete(image)

        # 새로운 이미지 추가
        for image in images:
            image_path = save_image(image, 'news')
            news_img = NewsImg(image_path=image_path, folder='news')
            news.images.append(news_img)

        news.modify_date = datetime.now()
        db.session.commit()

        return redirect(url_for('news.NewsDef'))
    else:
        return render_template('News/edit_news.html', news=news)
    

@bp.route('/News/delete/<int:news_id>')
@login_required
def delete(news_id):
    news = News.query.get_or_404(news_id)
    news_img = NewsImg.query.filter_by(news_id=news.id).all()
    for image in news_img:
        db.session.delete(image)
    db.session.delete(news)
    db.session.commit()
    return redirect(url_for('news.NewsDef'))