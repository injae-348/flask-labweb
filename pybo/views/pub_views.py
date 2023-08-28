from datetime import datetime
from flask import Blueprint, render_template, url_for,request
from werkzeug.utils import redirect

from pybo.models import Publications
from pybo import db

bp = Blueprint('pub',__name__,url_prefix='/Publications')
from pybo.views.auth_views import login_required

@bp.route('/Publications_Domestic_Conferences')
def PubDomConfDef():
    publicationsList = Publications.query.order_by(Publications.date.desc())
    return render_template('Publications/pub_dom_conf.html',publicationsList=publicationsList)

@bp.route('/Publications_Domestic_Journals')
def PubDomJournDef():
    publicationsList = Publications.query.order_by(Publications.date.desc())
    return render_template('Publications/pub_dom_journ.html',publicationsList=publicationsList)

@bp.route('/Publications_Domestic_Patents')
def PubDomPatenDef():
    publicationsList = Publications.query.order_by(Publications.date.desc())
    return render_template('Publications/pub_dom_paten.html',publicationsList=publicationsList)



@bp.route('/Publications_International_Conferences')
def PubInConfDef():
    publicationsList = Publications.query.order_by(Publications.date.desc())
    return render_template('Publications/pub_in_conf.html',publicationsList=publicationsList)

@bp.route('/Publications_International_Journals')
def PubInJournDef():
    publicationsList = Publications.query.order_by(Publications.date.desc())    
    return render_template('Publications/pub_in_journ.html',publicationsList=publicationsList)

@bp.route('/Publications_International_Patents')
def PubInPatenDef():
    publicationsList = Publications.query.order_by(Publications.date.desc())
    return render_template('Publications/pub_in_paten.html',publicationsList=publicationsList)


@bp.route('/Publications/create',methods=['GET','POST'])
@login_required
def create_publication():
    if request.method == 'POST':
        date = request.form['date']
        title = request.form['title']
        author = request.form['author']
        read_more = request.form['read_more']
        category = request.form['category']
        create_date = datetime.now()

        new_pub = Publications(date=date,title=title,author=author,read_more=read_more,category=category,create_date=create_date)
        db.session.add(new_pub)
        db.session.commit()


        # 각각의 생성 페이지로 rendering 되면 좋긴한데
        # 지금 상태를 보니 type 이랑 category를 설정했으면 가능했을듯 한데 지금 상태에서는 그냥 하기
        # 아래처럼 짜보면 되긴 할듯
        # if request.method == 'POST':
        # 데이터베이스에 새로운 항목 추가하는 코드
        # publication_type = request.form['type']  # 선택한 종류
        # publication_category = request.form['category']  # 선택한 카테고리
        # URL을 기반으로 템플릿 파일의 경로 생성
        # publication_path = url_for('static', filename=f'Publications/pub_{publication_type}_{publication_category}.html')
        # return render_template(publication_path)

        _next = request.args.get('next','')
        if _next:
            return redirect(_next)
        else:
            return redirect(url_for('pub.PubInJournDef'))
    
    previous_url = request.referrer
    return render_template('Publications/create_pub.html',previous_url=previous_url)
    
@bp.route('/Publications/modify/<int:pub_id>',methods=('GET','POST'))
@login_required
def modify(pub_id):
    publications = Publications.query.get_or_404(pub_id)
    if request.method == 'POST':
        date = request.form['date']
        title = request.form['title']
        author = request.form['author']
        read_more = request.form['read_more']
        category = request.form['category']

        publications.date = date
        publications.title = title
        publications.author = author
        publications.read_more = read_more
        publications.category = category
        publications.modify_date = datetime.now()
        db.session.commit()
        return redirect(url_for('pub.PubInJournDef'))
    return render_template('Publications/edit_pub.html',publications=publications)

@bp.route('/Publications/delete/<int:pub_id>')
@login_required
def delete(pub_id):
    publications = Publications.query.get_or_404(pub_id)
    db.session.delete(publications)
    db.session.commit()
    return redirect(url_for('pub.PubInJournDef'))