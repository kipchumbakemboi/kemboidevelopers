from wtforms.validators import ValidationError
import re

def validate_email(form, field):
    """Validate email format"""
    email = field.data
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValidationError('Invalid email address')

def validate_phone_number(form, field):
    """Validate phone number"""
    phone = field.data
    if phone and not re.match(r'^(\+254|0)[17]\d{8}$', phone):
        raise ValidationError('Invalid Kenyan phone number format')
