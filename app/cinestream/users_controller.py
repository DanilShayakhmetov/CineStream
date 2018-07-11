import os
from flask import render_template, Blueprint, redirect, request, url_for, app, send_from_directory
from flask_login import login_user, current_user, login_required, logout_user
from datetime import datetime
from werkzeug.utils import secure_filename
from cinestream.config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from .database import db
from .models import UserProfile
from cinestream.forms import RegisterForm, LoginForm, EditProfileForm


users_blueprint = Blueprint('users', __name__, template_folder='templates')
UPLOAD_FOLDER2 = 'images/users'


@users_blueprint.route('/users')
def users():
    all_users = UserProfile.query.order_by(UserProfile.firstName).all()
    return render_template('users/users.html', all_users=all_users)


@users_blueprint.route('/login', methods=['GET'])
def login_template():
    form = LoginForm(request.form)
    return render_template('users/login.html', form=form)


@users_blueprint.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = UserProfile.query.filter_by(email=form.email.data).first()
        if user is not None and user.is_correct_password(form.password.data):
            user.authenticated = True
            user.last_logged_in = user.current_logged_in
            user.current_logged_in = datetime.now()
            db.session.add(user)
            db.session.commit()
            login_user(user)
            print('Thanks for logging in, {}'.format(current_user.email))
            return redirect(url_for('users.user_profile'))
        else:
            print('ERROR! Incorrect login credentials.', 'error')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@users_blueprint.route('/register', methods=['GET'])
def register_template():
    form = RegisterForm(request.form)
    return render_template('users/register.html', form=form)


@users_blueprint.route('/register', methods=['POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            print('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        if form.validate_on_submit():
            new_user = new_user_parsing(form, filename)
            new_user.authenticated = True
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            print('Thanks for registering!', 'success')
            return redirect(url_for('users.user_profile'))


def new_user_parsing(form, filename):
    path = UPLOAD_FOLDER2 + '/' + filename
    new_user_params = UserProfile({
        'email': form.email.data,
        'plaintext_password': form.password.data,
        'firstName': form.firstName.data,
        'lastName': form.lastName.data,
        'city': form.city.data,
        'path': path,
    })
    return new_user_params


def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@users_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))


@users_blueprint.route('/user/profile')
@login_required
def user_profile():
    return render_template('users/user_profile.html')


@users_blueprint.route('/user/edit_profile', methods=['GET'])
@login_required
def edit_profile_template():
    form = EditProfileForm(request.form)
    form.email.data = current_user.email
    form.firstName.data = current_user.firstName
    form.lastName.data = current_user.lastName
    form.city.data = current_user.city
    return render_template('users/user_profile_editor.html', form=form)


@users_blueprint.route('/user/edit_profile', methods=['POST'])
@login_required
def edit_profile():
    form = EditProfileForm(request.form)
    try:
        file = request.files['file']
        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        path = UPLOAD_FOLDER2 + '/' + filename
        current_user.path = path
    except:
        print('no new file')

    current_user.email = form.email.data
    current_user.firstName = form.firstName.data
    current_user.lastName = form.lastName.data
    current_user.city = form.city.data

    db.session.commit()
    print('Your changes have been saved.')
    return redirect(url_for('users.user_profile'))
