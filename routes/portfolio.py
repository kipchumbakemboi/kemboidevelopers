from flask import Blueprint, render_template
from models.project import Project

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/')
def index():
    projects = Project.query.filter_by(featured=True).all()
    return render_template('public/portfolio.html', projects=projects)
