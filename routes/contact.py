from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import db
from models.contact import ContactMessage
from services.notification_service import notify_admin

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        contact_msg = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        db.session.add(contact_msg)
        db.session.commit()
        
        # Notify admin
        notify_admin(
            f"New Contact Message: {subject}",
            f"From: {name} ({email})\n\n{message}"
        )
        
        flash('Thank you! Your message has been sent.', 'success')
        return redirect(url_for('public.contact'))
    
    return render_template('public/contact.html')
