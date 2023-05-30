from flask import Blueprint, render_template
from pybo.views.auth_views import login_required
bp = Blueprint('index',__name__,url_prefix='')

from pybo.models import News

@bp.route('/Index')
def mainpage():
    newsList = News.query.order_by(News.activity_date.desc()).all()
    return render_template('Index/index.html',newsList=newsList)