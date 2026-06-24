import re
from slugify import slugify as python_slugify

def generate_slug(text):
    """Generate URL-friendly slug"""
    return python_slugify(text)

def format_currency(amount):
    """Format amount in Kenyan Shillings"""
    return f"KES {amount:,.2f}"

def truncate_text(text, length=100):
    """Truncate text with ellipsis"""
    if len(text) <= length:
        return text
    return text[:length].rsplit(' ', 1)[0] + '...'

def validate_phone(phone):
    """Validate Kenyan phone number"""
    pattern = r'^(\+254|0)[17]\d{8}$'
    return bool(re.match(pattern, phone))
