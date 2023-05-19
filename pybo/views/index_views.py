from flask import Blueprint, render_template

bp = Blueprint('index',__name__,url_prefix='')

@bp.route('/Index')
def mainpage():
    return render_template('Index/index.html')