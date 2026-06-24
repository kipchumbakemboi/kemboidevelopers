from flask import Blueprint, render_template
from models.project import Project
from models.blog import BlogPost

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def index():
    featured_projects = Project.query.filter_by(featured=True).limit(6).all()
    recent_posts = BlogPost.query.filter_by(published=True).order_by(BlogPost.created_at.desc()).limit(3).all()
    return render_template('public/index.html', 
                         featured_projects=featured_projects,
                         recent_posts=recent_posts)

@public_bp.route('/about')
def about():
    return render_template('public/about.html')

@public_bp.route('/services')
def services():
    return render_template('public/services.html')

@public_bp.route('/portfolio')
def portfolio():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('public/portfolio.html', projects=projects)

@public_bp.route('/blog')
def blog():
    posts = BlogPost.query.filter_by(published=True).order_by(BlogPost.created_at.desc()).all()
    return render_template('public/blog.html', posts=posts)

@public_bp.route('/contact')
def contact():
    return render_template('public/contact.html')

@public_bp.route('/faq')
def faq():
    return render_template('public/faq.html')

@public_bp.route('/testimonials')
def testimonials():
    return render_template('public/testimonials.html')

@public_bp.route('/quote')
def quote():
    return render_template('public/quote.html')
