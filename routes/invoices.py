from flask import Blueprint, render_template, send_file, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import db
from models.invoice import Invoice
from models.project import Project
from services.invoice_service import generate_invoice_pdf
from datetime import datetime, timedelta
import uuid

invoices_bp = Blueprint('invoices', __name__)

@invoices_bp.route('/')
@login_required
def list():
    if current_user.role == 'admin':
        invoices = Invoice.query.all()
    else:
        invoices = Invoice.query.filter_by(user_id=current_user.id).all()
    return render_template('invoices/list.html', invoices=invoices)

@invoices_bp.route('/<int:id>/pdf')
@login_required
def download_pdf(id):
    invoice = Invoice.query.get_or_404(id)
    project = invoice.project
    
    if current_user.role != 'admin' and invoice.user_id != current_user.id:
        flash("Unauthorized", "error")
        return redirect(url_for('invoices.list'))
    
    pdf_buffer = generate_invoice_pdf(invoice, project, invoice.user)
    
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=f"invoice_{invoice.invoice_number}.pdf",
        mimetype='application/pdf'
    )

@invoices_bp.route('/create/<int:project_id>', methods=['GET', 'POST'])
@login_required
def create(project_id):
    project = Project.query.get_or_404(project_id)
    
    if request.method == 'POST':
        amount = float(request.form.get('amount'))
        
        invoice = Invoice(
            invoice_number=f"INV-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:6].upper()}",
            project_id=project_id,
            user_id=project.client_id,
            amount=amount,
            due_date=datetime.utcnow() + timedelta(days=14),
            status='pending'
        )
        db.session.add(invoice)
        db.session.commit()
        
        flash("Invoice created successfully!", "success")
        return redirect(url_for('invoices.list'))
    
    return render_template('invoices/create.html', project=project)