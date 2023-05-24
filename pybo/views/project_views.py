from datetime import datetime
from flask import Blueprint, render_template, url_for,request
from werkzeug.utils import redirect

from pybo.models import Projects
from pybo import db

from pybo.utils import save_image,delete_image
from pybo.views.auth_views import login_required

bp = Blueprint('projects',__name__,url_prefix='')

@bp.route('/Projects')
def ProjectDef():
    projectsList = Projects.query.order_by(Projects.create_date.desc())
    return render_template('Projects/project.html',projectsList=projectsList)

@bp.route('/Projects/create', methods=['GET','POST'])
@login_required
def create_project():
    if request.method == 'POST':
        title = request.form['title']
        duration = request.form['duration']
        Agency = request.form['Agency']
        create_date = datetime.now()
        period = request.form['period']
        
        file = request.files['image']
        file_path = save_image(file,'projects')
        
        new_proj = Projects(title=title,duration=duration,Agency=Agency,image_path=file_path,period=period,folder='projects',create_date=create_date)
        db.session.add(new_proj)
        db.session.commit()

        return redirect(url_for('projects.ProjectDef'))
    else:
        return render_template('Projects/create_proj.html')

@bp.route('/Projects/modify/<int:projects_id>',methods=('GET','POST'))
@login_required
def modify(projects_id):
    projects = Projects.query.get_or_404(projects_id)

    if request.method =='POST':
        title = request.form['title']
        duration = request.form['duration']
        Agency = request.form['Agency']
        period = request.form['period']
        
        projects.title = title
        projects.duration = duration
        projects.Agency = Agency
        projects.period = period

        if 'image' in request.files:
            file = request.files['image']
            if file.filename != '':
                delete_image(projects.folder,projects.image_path)
                file_path = save_image(file,'projects')
                projects.image_path = file_path
        projects.modify_date = datetime.now()
        db.session.commit()
        return redirect(url_for('projects.ProjectDef'))
    return render_template('Projects/edit_projects.html',projects=projects)


@bp.route('/Projects/delete/<int:projects_id>')
@login_required
def delete(projects_id):
    projects = Projects.query.get_or_404(projects_id)
    db.session.delete(projects)
    db.session.commit()
    return redirect(url_for('projects.ProjectDef'))