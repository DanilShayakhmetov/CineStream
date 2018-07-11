from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('config.py')

import cinestream.views

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"


from cinestream.models import UserProfile


@login_manager.user_loader
def load_user(user_id):
    return UserProfile.query.filter(UserProfile.id == int(user_id)).first()
