from flask import Blueprint, render_template

bp = Blueprint('contact',__name__,url_prefix='')

@bp.route('/Contact')
def ContactDef():
    return render_template('Contact/contact.html')