from flask import Blueprint, render_template
from flask_login import login_required
from utils.decorators import admin_required
from models import db
from models.user import User
from models.project import Project
from models.review import Review

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/')
@login_required
@admin_required
def dashboard():
    total_users = User.query.count()
    active_projects = Project.query.filter(Project.status.in_(['in_progress', 'review'])).count()
    completed = Project.query.filter_by(status='completed').count()
    in_progress = Project.query.filter_by(status='in_progress').count()
    review = Project.query.filter_by(status='review').count()
    planning = Project.query.filter_by(status='planning').count()
    
    revenue = 2840000  # Placeholder
    avg_rating = 4.8
    
    return render_template('admin/analytics.html',
                         total_users=total_users,
                         active_projects=active_projects,
                         completed=completed,
                         in_progress=in_progress,
                         review=review,
                         planning=planning,
                         revenue=revenue,
                         avg_rating=avg_rating)
