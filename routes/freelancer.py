from flask import Blueprint, render_template
from flask_login import login_required

freelancer_bp = Blueprint('freelancer', __name__)

@freelancer_bp.route('/')
def index():
    return render_template('public/freelancers.html')

@freelancer_bp.route('/<int:id>')
@login_required
def profile(id):
    return render_template('public/freelancer_profile.html')
