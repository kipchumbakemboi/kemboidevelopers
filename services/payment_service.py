import requests
import base64
import json
from datetime import datetime
from flask import current_app

class MPesaService:
    def __init__(self):
        self.consumer_key = current_app.config.get('MPESA_CONSUMER_KEY')
        self.consumer_secret = current_app.config.get('MPESA_CONSUMER_SECRET')
        self.shortcode = current_app.config.get('MPESA_SHORTCODE')
        self.passkey = current_app.config.get('MPESA_PASSKEY')
        self.base_url = 'https://sandbox.safaricom.co.ke'  # Change to production when ready

    def get_access_token(self):
        """Get OAuth access token from Safaricom"""
        url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
        encoded = base64.b64encode(f"{self.consumer_key}:{self.consumer_secret}".encode()).decode()
        
        headers = {
            'Authorization': f'Basic {encoded}'
        }
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('access_token')
        return None

    def stk_push(self, phone, amount, account_ref, description):
        """Initiate STK Push payment"""
        access_token = self.get_access_token()
        if not access_token:
            return {'error': 'Failed to get access token'}
        
        url = f"{self.base_url}/mpesa/stkpush/v1/processrequest"
        
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode(
            f"{self.shortcode}{self.passkey}{timestamp}".encode()
        ).decode()
        
        payload = {
            "BusinessShortCode": self.shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": self.shortcode,
            "PhoneNumber": phone,
            "CallBackURL": "https://yourdomain.com/mpesa/callback",
            "AccountReference": account_ref,
            "TransactionDesc": description
        }
        
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
