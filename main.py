from flask import Flask,Blueprint,request

app = Flask(__name__)
email_bp = Blueprint('email_bp', __name__)
@email_bp.route('/api/email',methods=['POST'])
def get_emails():
    emails = request.get_json()
    print(emails)
    return emails
app.register_blueprint(email_bp)

if __name__ == '__main__':
    app.run()