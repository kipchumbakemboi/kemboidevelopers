from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db
from models.project import Project

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/')
@login_required
def list():
    if current_user.role == 'client':
        projects = Project.query.filter_by(client_id=current_user.id).all()
    elif current_user.role == 'freelancer':
        projects = Project.query.filter_by(freelancer_id=current_user.id).all()
    else:
        projects = Project.query.all()
    return render_template('dashboard/projects.html', projects=projects)

@projects_bp.route('/kanban')
@login_required
def kanban():
    if current_user.role == 'client':
        projects = Project.query.filter_by(client_id=current_user.id).all()
    else:
        projects = Project.query.all()
    return render_template('dashboard/kanban.html', projects=projects)

@projects_bp.route('/<int:id>/update-status', methods=['POST'])
@login_required
def update_status(id):
    project = Project.query.get_or_404(id)
    new_status = request.form.get('status')
    project.status = new_status
    db.session.commit()
    return {'success': True}