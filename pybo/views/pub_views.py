from flask import Blueprint, render_template
from pybo.models import Publications
bp = Blueprint('pub',__name__,url_prefix='/Publications')

@bp.route('/Publications_Domestic_Conferences')
def PubDomConfDef():
    publicationsList = Publications.query.order_by(Publications.create_date.asc())
    return render_template('Publications/pub_dom_conf.html',publicationsList=publicationsList)

@bp.route('/Publications_Domestic_Journals')
def PubDomJournDef():
    publicationsList = Publications.query.order_by(Publications.create_date.asc())
    return render_template('Publications/pub_dom_journ.html',publicationsList=publicationsList)

@bp.route('/Publications_Domestic_Patents')
def PubDomPatenDef():
    publicationsList = Publications.query.order_by(Publications.create_date.asc())
    return render_template('Publications/pub_dom_paten.html',publicationsList=publicationsList)



@bp.route('/Publications_International_Conferences')
def PubInConfDef():
    publicationsList = Publications.query.order_by(Publications.create_date.asc())
    return render_template('Publications/pub_in_conf.html',publicationsList=publicationsList)

@bp.route('/Publications_International_Journals')
def PubInJournDef():
    publicationsList = Publications.query.order_by(Publications.create_date.asc())    
    return render_template('Publications/pub_in_journ.html',publicationsList=publicationsList)

@bp.route('/Publications_International_Patents')
def PubInPatenDef():
    publicationsList = Publications.query.order_by(Publications.create_date.asc())
    return render_template('Publications/pub_in_paten.html',publicationsList=publicationsList)


