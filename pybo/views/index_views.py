from flask import Blueprint, render_template
from pybo.views.auth_views import login_required
bp = Blueprint('index',__name__,url_prefix='')

@bp.route('/Index')
def mainpage():
    return render_template('Index/index.html')