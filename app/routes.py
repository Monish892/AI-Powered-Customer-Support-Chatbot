
import uuid
from flask import Blueprint, render_template, request, jsonify
from . import db, aiml_kernel
from .models import Conversation, Message, SenderType

# Create a Blueprint
main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    """Serves the main chat page."""
    return render_template('index.html')

@main_bp.route('/api/chat', methods=['POST'])
def chat():
    """Handles chat messages, interacts with AIML, and saves to the database."""
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Message not provided'}), 400

    user_message_content = data['message']
    conversation_id = data.get('conversation_id')

    try:
        # If no conversation_id, start a new one
        if not conversation_id:
            conversation_id = str(uuid.uuid4())
            new_conversation = Conversation(id=conversation_id)
            db.session.add(new_conversation)
        else:
            # Verify conversation exists
            conversation = db.session.get(Conversation, conversation_id)
            if not conversation:
                return jsonify({'error': 'Conversation not found'}), 404

        # Save user message
        user_message = Message(
            conversation_id=conversation_id,
            sender_type=SenderType.USER,
            content=user_message_content
        )
        db.session.add(user_message)

        # Get bot response from AIML kernel
        bot_response_content = aiml_kernel.get_response(user_message_content, conversation_id)

        # Save bot message
        bot_message = Message(
            conversation_id=conversation_id, 
            sender_type=SenderType.BOT, 
            content=bot_response_content
        )
        db.session.add(bot_message)

        # Commit all changes to the database
        db.session.commit()

        return jsonify({
            'response': bot_response_content,
            'conversation_id': conversation_id
        })

    except Exception as e:
        db.session.rollback()
        print(f"[CHAT-API-ERROR] {e}")
        return jsonify({'error': 'An internal error occurred'}), 500
