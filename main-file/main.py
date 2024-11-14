from flask import Flask

from blueprints.user_blueprint import user_bp
from blueprints.init_blueprint import init_bp
from inition import init

app = Flask(__name__)
init()
app.register_blueprint(init_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run()