from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=True)
    role = db.Column(db.String(20), default='client')
    full_name = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    bio = db.Column(db.Text)
    profile_pic = db.Column(db.String(200), default='default.png')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    # OAuth fields
    oauth_provider = db.Column(db.String(50))
    oauth_id = db.Column(db.String(255))
    
    # 2FA fields
    two_factor_secret = db.Column(db.String(32))
    two_factor_enabled = db.Column(db.Boolean, default=False)
    two_factor_verified = db.Column(db.Boolean, default=False)
    two_factor_backup_codes = db.Column(db.Text)
    
    # Relationships
    client_projects = db.relationship('Project', foreign_keys='Project.client_id', backref='client', lazy=True)
    freelancer_projects = db.relationship('Project', foreign_keys='Project.freelancer_id', backref='freelancer', lazy=True)
    quotes = db.relationship('Quote', backref='user', lazy=True)
    blog_posts = db.relationship('BlogPost', backref='author', lazy=True)
    
    __table_args__ = (
        db.UniqueConstraint('oauth_provider', 'oauth_id', name='uix_oauth'),
    )
    
    def set_password(self, password):
        if password:
            self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        if self.password_hash:
            return check_password_hash(self.password_hash, password)
        return False
    
    def __repr__(self):
        return f'<User {self.username}>'
