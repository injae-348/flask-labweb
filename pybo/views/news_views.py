import os
from datetime import datetime
from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect,secure_filename

from pybo.models import News,NewsImg
from pybo.forms import NewsForm
from pybo import db

from pybo.utils import save_image

bp = Blueprint('news',__name__,url_prefix='')

@bp.route('/News')
def NewsDef():
    newsList = News.query.order_by(News.create_date.asc()).all()
    return render_template('News/news.html',newsList=newsList)


@bp.route('/News/create', methods=['GET','POST'])
def create_news():
    if request.method == 'POST':
        activity_date = request.form['activity_date']
        activity = request.form['activity']
        content = request.form['content']
        images = request.files.getlist('images[]')
        create_date = datetime.now()
        new_news = News(activity_date=activity_date,activity=activity,content=content,create_date=create_date)

        for image in images:
            image_path = save_image(image)
            news_img = NewsImg(image_path=image_path)
            new_news.images.append(news_img)
            
        db.session.add(new_news)
        db.session.commit()
        
        return redirect(url_for('news.NewsDef'))
    else:
        return render_template('News/create_news.html')


'''
@bp.route('/News/create', methods=['GET', 'POST'])
def create_news():
    form = NewsForm()

    if request.method=='POST' and form.validate_on_submit():
        new_news = News(activity_date=form.activity_date.data, activity=form.activity.data, content=form.content.data, create_date=datetime.now())
        
        for file in form.images.data:
            file_name = secure_filename(file.file_name)
            file_path = os.path.join('pybo/static/img/portfolio',file_name)
            file.save(file_path)
            news_img = NewsImg(image_path=file_name)
            new_news.images.append(news_img)

        db.session.add(new_news)
        db.session.commit()
        return redirect(url_for('news.NewsDef'))

    return render_template('News/create_news.html', form=form)
'''