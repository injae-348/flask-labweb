from flask import Blueprint,url_for,render_template,request,flash,session,g
from werkzeug.utils import redirect
from pybo import db
from pybo.models import RootUser

import functools

bp = Blueprint('auth',__name__,url_prefix='')

@bp.route('/login/',methods=('GET','POST'))
def login():
    rootUser = RootUser.query.get(1)
    if request.method=='POST':
        error = None
        user = request.form['username']
        pw = request.form['password']

        if user != rootUser.username:
            error = '존재하지 않는 사용자입니다.'
        elif pw != rootUser.password:
            error = '비밀번호가 올바르지 않습니다.'
        if error is None:
            session.clear()
            session['user_id'] = rootUser.id
            # next를 지정해주었지만 잘 작동하지 않는다;;
            _next = request.args.get('next','')
            if _next:
                return redirect(_next)    
            else:
                return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html',rootUser=rootUser)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = RootUser.query.get(user_id)


@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args,**kwargs):
        if g.user is None:
            _next=request.url if request.method =='GET' else ''
            return redirect(url_for('auth.login',next=_next))
        return view(*args,**kwargs)
    return wrapped_view