from flask import Blueprint, render_template
from pybo.views.auth_views import login_required
bp = Blueprint('create_btn',__name__,url_prefix='')

@bp.route('/add')
def create_btn():
    return render_template('CreateClass/add.html')


# secret으로 따로 뺏는데 이렇게 안해도 될지도 모르겠다 