from extensions import db
from datetime import datetime

class Quote(db.Model):
    __tablename__ = 'quotes'
    
    id = db.Column(db.Integer, primary_key=True)
    project_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    budget_range = db.Column(db.String(50))
    timeline = db.Column(db.String(50))
    contact_method = db.Column(db.String(50))
    status = db.Column(db.String(20), default='pending')
    admin_notes = db.Column(db.Text)
    estimated_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
        return f'<Quote {self.id}>'
