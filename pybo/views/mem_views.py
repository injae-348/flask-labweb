from datetime import datetime
from flask import Blueprint, render_template,url_for,request
from werkzeug.utils import redirect

from pybo.models import MemberCurrent,MemberAlumni,Professor, Education, Career, ResearchPage
from pybo import db

# from pybo.utils import save_image,delete_image
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



@bp.route('/Professor/modify/<int:prof_id>', methods=('GET', 'POST'))
@login_required
def modify_prof(prof_id):
    professor = Professor.query.get_or_404(prof_id)
    education = Education.query.filter_by(professor_id=professor.id).all()
    career = Career.query.filter_by(professor_id=professor.id).all()
    researchPage = ResearchPage.query.filter_by(professor_id=professor.id).all()

    if request.method == 'POST':
        department = request.form['department']
        phone = request.form['phone']
        email = request.form['email']
        office_phone = request.form['office_phone']
        kaddress = request.form['kaddress']
        eaddress = request.form['eaddress']

        professor.department = department
        professor.phone = phone
        professor.email = email
        professor.office_phone = office_phone
        professor.kaddress = kaddress
        professor.eaddress = eaddress

        professor.modify_date = datetime.now()

        for edu in education:
            edu_id = edu.id
            Eperiod = request.form['Eperiod_' + str(edu_id)]
            Eedegree = request.form['Eedegree_' + str(edu_id)]
            Ekdegree = request.form['Ekdegree_' + str(edu_id)]
            EedegreeDetail = request.form['EedegreeDetail_' + str(edu_id)]

            edu.period = Eperiod
            edu.edegree = Eedegree
            edu.kdegree = Ekdegree
            edu.edegreeDetail = EedegreeDetail

        for car in career:
            car_id = car.id
            Cperiod = request.form['Cperiod_' + str(car_id)]
            Ceposition = request.form['Ceposition_' + str(car_id)]
            Ckposition = request.form['Ckposition_' + str(car_id)]
            CepositionDetail = request.form['CepositionDetail_' + str(car_id)]

            car.period = Cperiod
            car.eposition = Ceposition
            car.kposition = Ckposition
            car.epositionDetail = CepositionDetail

        for research in researchPage:
            research_id = research.id
            Rurl_path = request.form['url_path_' + str(research_id)]
            Rpage = request.form['page_' + str(research_id)]

            research.url_path = Rurl_path
            research.page = Rpage

        db.session.commit()

        return redirect(url_for('member.MemberProfDef'))

    return render_template('Members/edit_prof.html', professor=professor, education=education, career=career, researchPage=researchPage)

@bp.route('/Professor/create_education/<int:prof_id>',methods=('GET','POST'))
@login_required
def create_education(prof_id):
    if request.method == 'POST':
        period = request.form['period']
        edegree = request.form['edegree']
        kdegree = request.form['kdegree']
        edegreeDetail = request.form['edegreeDetail']

        edu = Education(professor_id=prof_id,period=period,edegree=edegree,kdegree=kdegree,edegreeDetail=edegreeDetail)

        db.session.add(edu)
        db.session.commit()

        return redirect(url_for('member.MemberProfDef'))
    return render_template('Members/create_edu.html')

@bp.route('/Professor/delete_education/<int:edu_id>')
@login_required
def delete_education(edu_id):
    edu = Education.query.get_or_404(edu_id)
    db.session.delete(edu)
    db.session.commit()
    return redirect(url_for('member.modify_prof',prof_id=1))


@bp.route('/Professor/create_career/<int:prof_id>',methods=('GET','POST'))
@login_required
def create_career(prof_id):
    if request.method == 'POST':
        period = request.form['period']
        eposition = request.form['eposition']
        kposition = request.form['kposition']
        epositionDetail = request.form['epositionDetail']

        career = Career(professor_id=prof_id,period=period,eposition=eposition,kposition=kposition,epositionDetail=epositionDetail)

        db.session.add(career)
        db.session.commit()
        return redirect(url_for('member.MemberProfDef'))
    return render_template('Members/create_career.html')

@bp.route('Professor/delete_career/<int:career_id>')
@login_required
def delete_career(career_id):
    career = Career.query.get_or_404(career_id)
    db.session.delete(career)
    db.session.commit()
    return redirect(url_for('member.modify_prof',prof_id=1))


@bp.route('Professor/create_research/<int:prof_id>',methods=('GET','POST'))
@login_required
def create_research(prof_id):
    if request.method == 'POST':
        url_path = request.form['url_path']
        page = request.form['page']

        research = ResearchPage(professor_id=prof_id,url_path=url_path,page=page)
        db.session.add(research)
        db.session.commit()
        return redirect(url_for('member.MemberProfDef'))
    return render_template('Members/create_research.html')

@bp.route('Professor/delete_research/<int:research_id>')
@login_required
def delete_research(research_id):
    research = ResearchPage.query.get_or_404(research_id)
    db.session.delete(research)
    db.session.commit()
    return redirect(url_for('member.modify_prof',prof_id=1))