from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import MemberCurrent, MemberAlumni

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('index.mainpage'))