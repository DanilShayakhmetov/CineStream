SECRET_KEY = 'N#\x82mB!\xa8\x1c.\xf8\x14\x1c<c\x17t\xa2\x03+\xd4\xea\x8eT7'
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost/user_profile'
SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_ENABLED = True

BCRYPT_LOG_ROUNDS = 15

ALLOWED_EXTENSIONS = ['jpg', 'png', 'jpeg', 'gif']
UPLOAD_FOLDER = 'cinestream/static/images/users'
