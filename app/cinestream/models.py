from cinestream.database import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property


class UserProfile(db.Model):
    __tablename__ = 'users_profile'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.Binary(60), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column(db.DateTime, nullable=True)
    last_logged_in = db.Column(db.DateTime, nullable=True)
    current_logged_in = db.Column(db.DateTime, nullable=True)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    path = db.Column(db.String, unique=True, nullable=False)



    def __init__(self, user_profile_params):
        self.email = user_profile_params['email']
        self.hashed_password = bcrypt.generate_password_hash(user_profile_params['plaintext_password'])
        self.authenticated = False
        self.firstName = user_profile_params['firstName']
        self.lastName = user_profile_params['lastName']
        self.city = user_profile_params['city']
        self.path = user_profile_params['path']


    @hybrid_property
    def password(self):
        return self.hashed_password

    @password.setter
    def set_password(self, plaintext_password):
        self.hashed_password = bcrypt.generate_password_hash(plaintext_password)

    @hybrid_method
    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password, plaintext_password)

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        """Requires use of Python 3"""
        return str(self.id)

    def __repr__(self):
        return '<User {0}>'.format(self.name)
