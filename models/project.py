from extensions import db
from datetime import datetime

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    freelancer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String(50))
    technologies = db.Column(db.String(200))
    image = db.Column(db.String(200))
    live_url = db.Column(db.String(300))
    github_url = db.Column(db.String(300))
    status = db.Column(db.String(20), default='planning')  # planning, todo, in_progress, review, completed, on_hold
    budget = db.Column(db.Float)
    deadline = db.Column(db.DateTime)
    progress = db.Column(db.Integer, default=0)
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships are defined on the User model to avoid ambiguity
    pass
    
    def __repr__(self):
        return f'<Project {self.title}>'
