from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import db
from models.review import Review
from models.project import Project
from models.user import User

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/project/<int:project_id>', methods=['GET', 'POST'])
@login_required
def create(project_id):
    project = Project.query.get_or_404(project_id)
    
    if request.method == 'POST':
        rating = int(request.form.get('rating'))
        comment = request.form.get('comment')
        
        review = Review(
            project_id=project_id,
            reviewer_id=current_user.id,
            reviewee_id=project.freelancer_id or project.client_id,
            rating=rating,
            comment=comment
        )
        db.session.add(review)
        db.session.commit()
        
        flash("Thank you for your review!", "success")
        return redirect(url_for('projects.list'))
    
    return render_template('reviews/create.html', project=project)

@reviews_bp.route('/freelancer/<int:user_id>')
def freelancer_reviews(user_id):
    reviews = Review.query.filter_by(reviewee_id=user_id).all()
    avg_rating = sum(r.rating for r in reviews) / len(reviews) if reviews else 0
    return render_template('reviews/freelancer.html', reviews=reviews, avg_rating=avg_rating, user_id=user_id)