from datetime import datetime
from flask import Blueprint, render_template,url_for,request
from werkzeug.utils import redirect

from pybo.models import MemberCurrent,MemberAlumni,Professor
from pybo import db

from pybo.utils import save_image,delete_image
from pybo.views.auth_views import login_required

bp = Blueprint('member',__name__,url_prefix='/Members')

#-------------------------------------------------------------
@bp.route('/Current_Student')
def MemberCurrentDef():
    memberCurrentList = MemberCurrent.query.order_by(MemberCurrent.create_date.desc())
    return render_template('Members/cur_stu.html',memberCurrentList=memberCurrentList)

@bp.route('/Current_Student/create',methods=['GET','POST'])
@login_required
def create_current_student():
    if request.method == 'POST':
        kname = request.form['kname']
        ename = request.form['ename']
        degree = request.form['degree']
        email = request.form['email']
        create_date = datetime.now()

        file = request.files['image']        
        # 파일 저장
        file_path = save_image(file,'member')
        new_current_student = MemberCurrent(kname=kname,ename=ename,degree=degree,email=email,image_path=file_path,folder='member',create_date=create_date)

        db.session.add(new_current_student)
        db.session.commit()

        return redirect(url_for('member.MemberCurrentDef'))
    else:
        return render_template('Members/create_cur.html')


@bp.route('/Current_Student/modify/<int:member_id>',methods=('GET','POST'))
@login_required
def modify_cur(member_id):
    member = MemberCurrent.query.get_or_404(member_id)

    if request.method == 'POST':
        kname = request.form['kname']
        ename = request.form['ename']
        degree = request.form['degree']
        email = request.form['email']

        member.kname = kname
        member.ename = ename
        member.degree = degree
        member.email = email

        if 'image' in request.files:
            file = request.files['image']
            if file.filename != '':
                delete_image(member.folder,member.image_path)
                file_path = save_image(file,'member')
                member.image_path = file_path
        
        member.modify_date = datetime.now()
        db.session.commit()
        return redirect(url_for('member.MemberCurrentDef'))
    return render_template('Members/edit_cur.html',member=member)


@bp.route('/Current_Student/delete/<int:member_id>',methods=('GET','POST'))
@login_required
def delete_cur(member_id):
    member = MemberCurrent.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('member.MemberCurrentDef'))


#-------------------------------------------------------------

@bp.route('/Alumni')
def MemberAlumniDef():
    memberAlumniList = MemberAlumni.query.order_by(MemberAlumni.create_date.desc())
    return render_template('Members/alumni.html',memberAlumniList=memberAlumniList)

@bp.route('/Alumni/create',methods=['GET','POST'])
@login_required
def create_alumni():
    if request.method == 'POST':
        kname = request.form['kname']
        ename = request.form['ename']
        degree = request.form['degree']
        company = request.form['company']
        create_date = datetime.now()

        file = request.files['image']        
        # 파일 저장
        file_path = save_image(file,'member')
        new_al = MemberAlumni(kname=kname,ename=ename,degree=degree,company=company,image_path=file_path,folder='member',create_date=create_date)

        db.session.add(new_al)
        db.session.commit()

        return redirect(url_for('member.MemberAlumniDef'))
    else:
        return render_template('Members/create_al.html')
        

@bp.route('/Alumni/modify/<int:member_id>',methods=('GET','POST'))
@login_required
def modify_al(member_id):
    member = MemberAlumni.query.get_or_404(member_id)

    if request.method == 'POST':
        kname = request.form['kname']
        ename = request.form['ename']
        degree = request.form['degree']
        company = request.form['company']

        member.kname = kname
        member.ename = ename
        member.degree = degree
        member.company = company

        if 'image' in request.files:
            file = request.files['image']
            if file.filename != '':
                delete_image(member.folder,member.image_path)
                file_path = save_image(file,'member')
                member.image_path = file_path
        # folder는 create시 자동으로 설정되므로 굳이 건들 필요 없다
        member.modify_date = datetime.now()
        db.session.commit()
        return redirect(url_for('member.MemberAlumniDef'))
    return render_template('Members/edit_al.html',member=member)


@bp.route('/Alumni/delete/<int:member_id>',methods=('GET','POST'))
@login_required
def delete_al(member_id):
    member = MemberAlumni.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('member.MemberAlumniDef'))


#-------------------------------------------------------------

@bp.route('/Professor')
def MemberProfDef():
    professor = Professor.query.get_or_404(1)
    return render_template('Members/professor.html',professor=professor)