"""
Kemboi Developers - Database Seeder
Run: python seed.py
"""

from app import create_app
from models import db
from models.user import User
from models.project import Project
from models.blog import BlogPost
from models.quote import Quote
from models.contact import ContactMessage
import random

app = create_app()

with app.app_context():
    print("🌱 Seeding Kemboi Developers database...\n")
    
    # === USERS ===
    print("Creating users...")
    
    # Admin
    admin = User.query.filter_by(email='admin@kemboidevelopers.com').first()
    if not admin:
        admin = User(
            username='admin',
            email='admin@kemboidevelopers.com',
            full_name='Admin User',
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)
    
    # Freelancers
    freelancers_data = [
        {"username": "gracewanjiku", "email": "grace@kemboi.dev", "full_name": "Grace Wanjiku", "role": "freelancer"},
        {"username": "michaelotieno", "email": "michael@kemboi.dev", "full_name": "Michael Otieno", "role": "freelancer"},
        {"username": "sarahkimani", "email": "sarah@kemboi.dev", "full_name": "Sarah Kimani", "role": "freelancer"},
    ]
    
    for f in freelancers_data:
        if not User.query.filter_by(email=f["email"]).first():
            user = User(**f)
            user.set_password("demo123")
            db.session.add(user)
    
    # Clients
    clients_data = [
        {"username": "equitybank", "email": "tech@equitybank.co.ke", "full_name": "Equity Bank", "role": "client"},
        {"username": "twigafoods", "email": "dev@twigafoods.com", "full_name": "Twiga Foods", "role": "client"},
        {"username": "cellulant", "email": "engineering@cellulant.com", "full_name": "Cellulant", "role": "client"},
    ]
    
    for c in clients_data:
        if not User.query.filter_by(email=c["email"]).first():
            user = User(**c)
            user.set_password("demo123")
            db.session.add(user)
    
    db.session.commit()
    
    # === PROJECTS ===
    print("Creating projects...")
    
    projects_data = [
        {
            "title": "Safaricom Enterprise Platform",
            "slug": "safaricom-enterprise-platform",
            "description": "Modern enterprise platform for Safaricom's internal operations.",
            "category": "Enterprise",
            "technologies": "React, Python, PostgreSQL, Kubernetes",
            "status": "completed",
            "featured": True,
            "budget": 2450000,
            "progress": 100
        },
        {
            "title": "Twiga Foods Mobile App",
            "slug": "twiga-foods-mobile-app",
            "description": "Cross-platform mobile application for supply chain management.",
            "category": "Mobile",
            "technologies": "Flutter, Node.js, MongoDB",
            "status": "in_progress",
            "featured": True,
            "budget": 980000,
            "progress": 67
        },
        {
            "title": "Equity Bank AI Chatbot",
            "slug": "equity-bank-ai-chatbot",
            "description": "Intelligent customer service chatbot powered by AI.",
            "category": "AI",
            "technologies": "Python, LangChain, Gemini, FastAPI",
            "status": "in_progress",
            "featured": True,
            "budget": 1450000,
            "progress": 42
        }
    ]
    
    clients = User.query.filter_by(role='client').all()
    freelancers = User.query.filter_by(role='freelancer').all()
    
    for p in projects_data:
        if not Project.query.filter_by(slug=p["slug"]).first():
            project = Project(**p)
            if clients:
                project.client_id = random.choice(clients).id
            if freelancers:
                project.freelancer_id = random.choice(freelancers).id
            db.session.add(project)
    
    db.session.commit()
    
    # === QUOTES ===
    print("Creating quote requests...")
    
    quotes_data = [
        {
            "project_type": "Enterprise Web Platform",
            "description": "We need a modern internal portal for 1200+ employees.",
            "budget_range": "KES 2M - 4M",
            "timeline": "4-6 months",
            "status": "pending"
        },
        {
            "project_type": "AI Solution",
            "description": "Customer support AI assistant with CRM and WhatsApp integration.",
            "budget_range": "KES 500K - 1.5M",
            "timeline": "2-3 months",
            "status": "reviewed"
        }
    ]
    
    for q in quotes_data:
        if clients and not Quote.query.filter_by(description=q["description"]).first():
            quote = Quote(**q)
            quote.user_id = random.choice(clients).id
            db.session.add(quote)
    
    db.session.commit()
    
    print("\n✅ Seeding complete!")
    print(f"   • Users: {User.query.count()}")
    print(f"   • Projects: {Project.query.count()}")
    print(f"   • Quotes: {Quote.query.count()}")