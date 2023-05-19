from flask import Blueprint, render_template

from pybo.models import MemberCurrent,MemberAlumni,Professor

bp = Blueprint('member',__name__,url_prefix='/Members')

@bp.route('/Current_Student')
def MemberCurrentDef():
    memberCurrentList = MemberCurrent.query.order_by(MemberCurrent.create_date.desc())
    return render_template('Members/cur_stu.html',memberCurrentList=memberCurrentList)

@bp.route('/Alumni')
def MemberAlumniDef():
    memberAlumniList = MemberAlumni.query.order_by(MemberAlumni.create_date.desc())
    return render_template('Members/alumni.html',memberAlumniList=memberAlumniList)

@bp.route('/Professor')
def MemberProfDef():
    professor = Professor.query.get_or_404(1)
    return render_template('Members/professor.html',professor=professor)