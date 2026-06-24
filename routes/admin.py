from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db
from models.user import User
from models.project import Project
from models.blog import BlogPost
from models.quote import Quote
from models.contact import ContactMessage
from utils.decorators import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    total_users = User.query.count()
    total_projects = Project.query.count()
    total_quotes = Quote.query.count()
    unread_messages = ContactMessage.query.filter_by(is_read=False).count()
    
    recent_users = User.query.order_by(User.created_at.desc()).limit(5).all()
    recent_quotes = Quote.query.order_by(Quote.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         total_users=total_users,
                         total_projects=total_projects,
                         total_quotes=total_quotes,
                         unread_messages=unread_messages,
                         recent_users=recent_users,
                         recent_quotes=recent_quotes)

@admin_bp.route('/users')
@login_required
@admin_required
def users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@admin_bp.route('/projects')
@login_required
@admin_required
def projects():
    projects = Project.query.all()
    return render_template('admin/projects.html', projects=projects)

@admin_bp.route('/messages')
@login_required
@admin_required
def messages():
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return render_template('admin/messages.html', messages=messages)

@admin_bp.route('/faqs')
@login_required
@admin_required
def faqs():
    return render_template('admin/faqs.html')

@admin_bp.route('/testimonials')
@login_required
@admin_required
def testimonials():
    return render_template('admin/testimonials.html')
