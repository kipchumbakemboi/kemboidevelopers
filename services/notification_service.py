from flask import current_app
from .email_service import send_email

def send_notification(user_email, subject, message):
    """Send notification to user"""
    try:
        send_email(user_email, subject, message)
        return True
    except Exception as e:
        print(f"[Notification] Error: {e}")
        return False

def notify_admin(subject, message):
    """Notify admin of important events (graceful failure)"""
    try:
        admin_email = current_app.config.get('MAIL_DEFAULT_SENDER')
        if admin_email:
            send_email(admin_email, subject, message)
            print(f"[Notification] Admin notified: {subject}")
    except Exception as e:
        print(f"[Notification] Failed to notify admin: {e}")
        # Don't crash the app if email fails
