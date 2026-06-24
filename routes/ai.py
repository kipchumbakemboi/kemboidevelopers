from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from services.ai_service import AIService

ai_bp = Blueprint('ai', __name__)
ai_service = AIService()

@ai_bp.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        message = request.json.get('message')
        if message:
            response = ai_service.chat_response(message)
            return jsonify({'response': response})
        return jsonify({'error': 'No message provided'}), 400
    
    return render_template('public/ai_chat.html')
