from flask import Flask, Blueprint, request, jsonify

from messages_producer.message_producer import send_message

app = Flask(__name__)
email_bp = Blueprint('email_bp', __name__)
@email_bp.route('/api/email',methods=['POST'])
def get_emails():
    email = request.get_json()
    send_message(email)
    return jsonify(email), 200
app.register_blueprint(email_bp)

if __name__ == '__main__':
    app.run()