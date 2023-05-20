from datetime import datetime
from flask import Blueprint, render_template,url_for,request
from werkzeug.utils import redirect

from pybo.models import MemberCurrent,MemberAlumni,Professor
from pybo import db

from pybo.utils import save_image

bp = Blueprint('member',__name__,url_prefix='/Members')

@bp.route('/Current_Student')
def MemberCurrentDef():
    memberCurrentList = MemberCurrent.query.order_by(MemberCurrent.create_date.desc())
    return render_template('Members/cur_stu.html',memberCurrentList=memberCurrentList)

@bp.route('/Current_Student/create',methods=['GET','POST'])
def create_current_student():
    if request.method == 'POST':
        kname = request.form['kname']
        ename = request.form['ename']
        degree = request.form['degree']
        email = request.form['email']
        create_date = datetime.now()

        file = request.files['image']        
        # 파일 저장
        file_path = save_image(file)
        new_current_student = MemberCurrent(kname=kname,ename=ename,degree=degree,email=email,image_path=file_path,create_date=create_date)

        db.session.add(new_current_student)
        db.session.commit()

        return redirect(url_for('member.MemberCurrentDef'))
    else:
        return render_template('Members/create_cur.html')

@bp.route('/Alumni')
def MemberAlumniDef():
    memberAlumniList = MemberAlumni.query.order_by(MemberAlumni.create_date.desc())
    return render_template('Members/alumni.html',memberAlumniList=memberAlumniList)

@bp.route('/Alumni/create',methods=['GET','POST'])
def create_alumni():
    if request.method == 'POST':
        kname = request.form['kname']
        ename = request.form['ename']
        degree = request.form['degree']
        company = request.form['company']
        create_date = datetime.now()

        file = request.files['image']        
        # 파일 저장
        file_path = save_image(file)
        new_al = MemberAlumni(kname=kname,ename=ename,degree=degree,company=company,image_path=file_path,create_date=create_date)

        db.session.add(new_al)
        db.session.commit()

        return redirect(url_for('member.MemberAlumniDef'))
    else:
        return render_template('Members/create_al.html')
        

@bp.route('/Professor')
def MemberProfDef():
    professor = Professor.query.get_or_404(1)
    return render_template('Members/professor.html',professor=professor)