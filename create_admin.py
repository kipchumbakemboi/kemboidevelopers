from app import create_app
from models import db
from models.user import User

app = create_app()

with app.app_context():
    # Create tables if they don't exist
    db.create_all()
    
    # Check if admin already exists
    existing_admin = User.query.filter_by(email='admin@kemboidevelopers.com').first()
    if existing_admin:
        print("⚠️  Admin user already exists!")
        print("Email: admin@kemboidevelopers.com")
        print("Password: admin123")
    else:
        # Create admin user
        admin = User(
            username='admin',
            email='admin@kemboidevelopers.com',
            full_name='Admin User',
            role='admin'
        )
        admin.set_password('admin123')
        
        db.session.add(admin)
        db.session.commit()
        
        print("✅ Admin user created successfully!")
        print("Email: admin@kemboidevelopers.com")
        print("Password: admin123")
    
    print("\nYou can now log in at: http://localhost:5000/auth/login")