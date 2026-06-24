from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user

notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/')
@login_required
def index():
    return render_template('notifications/index.html')

@notifications_bp.route('/count')
@login_required
def count():
    return jsonify({"count": 3})
