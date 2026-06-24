from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/client')
@login_required
def client():
    if current_user.role != 'client':
        return redirect(url_for('dashboard.freelancer'))
    return render_template('dashboard/client_dashboard.html')

@dashboard_bp.route('/freelancer')
@login_required
def freelancer():
    if current_user.role == 'client':
        return redirect(url_for('dashboard.client'))
    return render_template('dashboard/freelancer_dashboard.html')

@dashboard_bp.route('/profile')
@login_required
def profile():
    return render_template('dashboard/profile.html')
