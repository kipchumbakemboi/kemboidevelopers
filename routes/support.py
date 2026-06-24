from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

support_bp = Blueprint('support', __name__)

@support_bp.route('/')
@login_required
def index():
    return render_template('support/tickets.html')

@support_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        flash('Support ticket created successfully!', 'success')
        return redirect(url_for('support.index'))
    return render_template('support/create.html')
