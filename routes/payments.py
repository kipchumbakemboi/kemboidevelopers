from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from services.payment_service import MPesaService

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/initiate', methods=['POST'])
@login_required
def initiate():
    phone = request.form.get('phone')
    amount = request.form.get('amount')
    
    mpesa = MPesaService()
    result = mpesa.stk_push(phone, amount, "Kemboi Project", "Project Payment")
    
    return jsonify(result)
