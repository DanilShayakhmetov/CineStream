from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from cinestream import app


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
