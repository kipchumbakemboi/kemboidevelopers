from extensions import socketio
from flask_socketio import emit, join_room, leave_room
from flask_login import current_user
from models.message import Message
from models import db

@socketio.on('connect')
def handle_connect():
    if current_user.is_authenticated:
        join_room(f'user_{current_user.id}')
        print(f"User {current_user.id} connected")

@socketio.on('disconnect')
def handle_disconnect():
    if current_user.is_authenticated:
        leave_room(f'user_{current_user.id}')

@socketio.on('send_message')
def handle_send_message(data):
    if not current_user.is_authenticated:
        return
    
    receiver_id = data.get('receiver_id')
    content = data.get('content')
    
    if not receiver_id or not content:
        return
    
    # Save message to database
    msg = Message(
        sender_id=current_user.id,
        receiver_id=receiver_id,
        content=content
    )
    db.session.add(msg)
    db.session.commit()
    
    # Emit to both users
    emit('new_message', {
        'id': msg.id,
        'sender_id': current_user.id,
        'content': content,
        'created_at': msg.created_at.strftime('%H:%M')
    }, room=f'user_{receiver_id}')
    
    emit('new_message', {
        'id': msg.id,
        'sender_id': current_user.id,
        'content': content,
        'created_at': msg.created_at.strftime('%H:%M')
    }, room=f'user_{current_user.id}')