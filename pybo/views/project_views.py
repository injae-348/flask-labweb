from flask import Blueprint, render_template
from pybo.models import Projects
bp = Blueprint('projects',__name__,url_prefix='')

@bp.route('/Projects')
def ProjectDef():
    projectsList = Projects.query.order_by(Projects.create_date.asc())
    return render_template('Projects/project.html',projectsList=projectsList)