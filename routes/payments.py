from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from services.payment_service import MPesaService

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/pay')
@login_required
def pay():
    return render_template('payments/pay.html')

@payments_bp.route('/initiate', methods=['POST'])
@login_required
def initiate():
    phone = request.form.get('phone')
    amount = request.form.get('amount')
    reference = request.form.get('reference', f"KEMBOI-{current_user.id}")

    if not phone or not amount:
        flash("Phone number and amount are required", "error")
        return redirect(url_for('payments.pay'))

    mpesa = MPesaService()
    result = mpesa.stk_push(phone, amount, reference, "Kemboi Developers Payment")

    if 'ResponseCode' in result and result['ResponseCode'] == '0':
        flash("STK Push sent! Please check your phone.", "success")
    else:
        flash("Payment initiation failed. Please try again.", "error")

    return redirect(url_for('payments.pay'))

@payments_bp.route('/callback', methods=['POST'])
def callback():
    """M-Pesa Callback Endpoint"""
    data = request.get_json()
    # TODO: Process payment confirmation here (update invoice status, etc.)
    print("M-Pesa Callback Received:", data)
    return jsonify({"ResultCode": 0, "ResultDesc": "Success"})