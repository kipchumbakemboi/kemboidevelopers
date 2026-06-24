from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db
from models.blog import BlogPost
from utils.helpers import generate_slug
import uuid

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/<slug>')
def post(slug):
    post = BlogPost.query.filter_by(slug=slug, published=True).first_or_404()
    return render_template('public/blog_post.html', post=post)

@blog_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        excerpt = request.form.get('excerpt')
        category = request.form.get('category')
        
        post = BlogPost(
            title=title,
            slug=generate_slug(title) + '-' + str(uuid.uuid4())[:8],
            content=content,
            excerpt=excerpt,
            category=category,
            author_id=current_user.id,
            published=True
        )
        
        db.session.add(post)
        db.session.commit()
        
        flash('Blog post created successfully!', 'success')
        return redirect(url_for('public.blog'))
    
    return render_template('blog/create.html')

@blog_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = BlogPost.query.get_or_404(id)
    
    if post.author_id != current_user.id and current_user.role != 'admin':
        flash('Unauthorized', 'error')
        return redirect(url_for('public.blog'))
    
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        post.excerpt = request.form.get('excerpt')
        post.category = request.form.get('category')
        
        db.session.commit()
        flash('Post updated!', 'success')
        return redirect(url_for('blog.post', slug=post.slug))
    
    return render_template('blog/edit.html', post=post)
