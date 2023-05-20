from datetime import datetime
from flask import Blueprint, render_template, url_for,request
from werkzeug.utils import redirect

from pybo.models import Projects
from pybo import db

from pybo.utils import save_image

bp = Blueprint('projects',__name__,url_prefix='')

@bp.route('/Projects')
def ProjectDef():
    projectsList = Projects.query.order_by(Projects.create_date.desc())
    return render_template('Projects/project.html',projectsList=projectsList)

@bp.route('/Projects/create', methods=['GET','POST'])
def create_project():
    if request.method == 'POST':
        title = request.form['title']
        duration = request.form['duration']
        Agency = request.form['Agency']
        create_date = datetime.now()
        period = request.form['period']
        
        file = request.files['image']
        file_path = save_image(file)
        
        new_proj = Projects(title=title,duration=duration,Agency=Agency,image_path=file_path,period=period,create_date=create_date)
        db.session.add(new_proj)
        db.session.commit()

        return redirect(url_for('projects.ProjectDef'))
    else:
        return render_template('Projects/create_proj.html')
