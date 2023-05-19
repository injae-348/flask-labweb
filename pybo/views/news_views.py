from datetime import datetime
from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect

from pybo.models import News,NewsImg
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