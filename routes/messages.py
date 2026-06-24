from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models import db
from models.message import Message
from models.user import User

messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/')
@login_required
def inbox():
    # Get all conversations
    sent = Message.query.filter_by(sender_id=current_user.id).all()
    received = Message.query.filter_by(receiver_id=current_user.id).all()
    
    # Get unique users
    user_ids = set()
    for m in sent:
        user_ids.add(m.receiver_id)
    for m in received:
        user_ids.add(m.sender_id)
    
    conversations = User.query.filter(User.id.in_(user_ids)).all() if user_ids else []
    
    return render_template('messages/inbox.html', conversations=conversations)

@messages_bp.route('/chat/<int:user_id>')
@login_required
def chat(user_id):
    other_user = User.query.get_or_404(user_id)
    
    # Get conversation
    messages = Message.query.filter(
        ((Message.sender_id == current_user.id) & (Message.receiver_id == user_id)) |
        ((Message.sender_id == user_id) & (Message.receiver_id == current_user.id))
    ).order_by(Message.created_at.asc()).all()
    
    # Mark as read
    Message.query.filter_by(receiver_id=current_user.id, sender_id=user_id, is_read=False).update({'is_read': True})
    db.session.commit()
    
    return render_template('messages/chat.html', other_user=other_user, messages=messages)

@messages_bp.route('/send', methods=['POST'])
@login_required
def send_message():
    receiver_id = request.form.get('receiver_id', type=int)
    content = request.form.get('content')
    
    if not receiver_id or not content:
        return jsonify({'error': 'Missing data'}), 400
    
    msg = Message(
        sender_id=current_user.id,
        receiver_id=receiver_id,
        content=content
    )
    db.session.add(msg)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message_id': msg.id,
        'created_at': msg.created_at.strftime('%H:%M')
    })
