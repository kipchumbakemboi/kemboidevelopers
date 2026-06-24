from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import db
from models.quote import Quote
from services.notification_service import notify_admin

quote_bp = Blueprint('quote', __name__)

@quote_bp.route('/', methods=['GET', 'POST'])
@login_required
def request_quote():
    if request.method == 'POST':
        project_type = request.form.get('project_type')
        description = request.form.get('description')
        budget_range = request.form.get('budget_range')
        timeline = request.form.get('timeline')
        contact_method = request.form.get('contact_method')
        
        quote = Quote(
            project_type=project_type,
            description=description,
            budget_range=budget_range,
            timeline=timeline,
            contact_method=contact_method,
            user_id=current_user.id
        )
        
        db.session.add(quote)
        db.session.commit()
        
        # Notify admin (non-blocking)
        try:
            notify_admin(
                "New Quote Request",
                f"Project: {project_type}\nUser: {current_user.email}\nBudget: {budget_range}\nTimeline: {timeline}"
            )
        except:
            pass  # Email is optional
        
        flash('Quote request submitted successfully! We will contact you soon.', 'success')
        return redirect(url_for('public.quote'))
    
    return render_template('public/quote.html')
