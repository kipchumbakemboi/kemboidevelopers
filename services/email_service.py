import os
from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def init_mail(app):
    mail.init_app(app)

def send_email(to, subject, template, **kwargs):
    """Send email using Flask-Mail (graceful failure)"""
    try:
        msg = Message(
            subject,
            recipients=[to],
            sender=current_app.config.get('MAIL_DEFAULT_SENDER')
        )
        msg.body = template
        mail.send(msg)
        return True
    except Exception as e:
        print(f"[Email] Failed to send email: {e}")
        print("[Email] Tip: Use Gmail App Password if using Gmail")
        return False
