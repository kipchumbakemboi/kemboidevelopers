from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from io import BytesIO
from datetime import datetime

def generate_invoice_pdf(invoice, project, user):
    """Generate a professional invoice PDF"""
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    
    # Header
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, height - 60, "KEMBOI DEVELOPERS")
    
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 80, "Premium Software & Consultancy")
    c.drawString(50, height - 95, "Nairobi, Kenya | hello@kemboidevelopers.com")
    
    # Invoice details
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 140, f"INVOICE #{invoice.invoice_number}")
    
    c.setFont("Helvetica", 11)
    c.drawString(50, height - 170, f"Date: {invoice.created_at.strftime('%B %d, %Y')}")
    c.drawString(50, height - 185, f"Due Date: {invoice.due_date.strftime('%B %d, %Y') if invoice.due_date else 'N/A'}")
    
    # Bill To
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, height - 230, "BILL TO:")
    c.setFont("Helvetica", 11)
    c.drawString(50, height - 250, user.full_name or user.username)
    c.drawString(50, height - 265, user.email)
    
    # Project info
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, height - 310, "PROJECT:")
    c.setFont("Helvetica", 11)
    c.drawString(50, height - 330, project.title)
    
    # Amount
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 380, f"TOTAL DUE: KES {invoice.amount:,.2f}")
    
    # Status
    c.setFont("Helvetica", 11)
    c.drawString(50, height - 410, f"Status: {invoice.status.upper()}")
    
    # Footer
    c.setFont("Helvetica", 9)
    c.drawString(50, 80, "Thank you for choosing Kemboi Developers.")
    c.drawString(50, 65, "Payment via M-Pesa: +254 700 123 456")
    
    c.save()
    buffer.seek(0)
    return buffer