from flask import Blueprint, request, jsonify
from help_dir.message_producer import send_message,check_suspicious_word

init_bp = Blueprint('init_bp', __name__)

@init_bp.route('/api/email',methods=['POST'])
def get_emails():
    email = request.get_json()
    send_message(email)
    check_suspicious_word(email)
    return jsonify(email), 200