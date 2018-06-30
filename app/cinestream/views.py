from flask import render_template
from cinestream import app
# from cinestream.config import EXTERNAL_LINKS, SOCIAL_LINKS
from cinestream.users_controller import users_blueprint


UPLOAD_FOLDER = 'cinestream/static/images/users'
UPLOAD_FOLDER2 = 'images/users'

app.register_blueprint(users_blueprint)


# @app.context_processor
# def inject_stuff():
#     return {'external_links': EXTERNAL_LINKS, 'social_links': SOCIAL_LINKS}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/platform/faq')
def platform_faq():
    return render_template('platform/faq.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')
