def register_blueprints(app):
    from .public import public_bp
    from .auth import auth_bp
    from .admin import admin_bp
    from .dashboard import dashboard_bp
    from .quote import quote_bp
    from .blog import blog_bp
    from .ai import ai_bp
    from .portfolio import portfolio_bp
    from .messages import messages_bp
    from .projects import projects_bp
    from .payments import payments_bp
    from .support import support_bp
    from .freelancer import freelancer_bp
    from .api import api_bp
    from .analytics import analytics_bp
    from .notifications import notifications_bp
    from .reviews import reviews_bp
    from .invoices import invoices_bp
    from .contact import contact_bp
    
    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(quote_bp, url_prefix='/quote')
    app.register_blueprint(blog_bp, url_prefix='/blog')
    app.register_blueprint(ai_bp, url_prefix='/ai')
    app.register_blueprint(portfolio_bp, url_prefix='/portfolio')
    app.register_blueprint(messages_bp, url_prefix='/messages')
    app.register_blueprint(projects_bp, url_prefix='/projects')
    app.register_blueprint(payments_bp, url_prefix='/payments')
    app.register_blueprint(support_bp, url_prefix='/support')
    app.register_blueprint(freelancer_bp, url_prefix='/freelancers')
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(analytics_bp, url_prefix='/analytics')
    app.register_blueprint(notifications_bp, url_prefix='/notifications')
    app.register_blueprint(reviews_bp, url_prefix='/reviews')
    app.register_blueprint(invoices_bp, url_prefix='/invoices')
    app.register_blueprint(contact_bp, url_prefix='/contact')
