from cinestream.models import UserProfile
from cinestream.database import db


users_profiles = [
    {
        'email': 'patkennedy79@gmail.com',
        'plaintext_password': '1',
        'firstName': 'Саша ',
        'lastName': 'Иванов',
        'city': 'Санкт-Петербург',
        'path': 'images/users/2.jpg'
    },
    {
        'email': 'ken@gmail.com',
        'plaintext_password': '1',
        'firstName': 'Катя',
        'lastName': 'Сергеева',
        'city': 'Москва',
        'path': 'images/users/1.jpg'

    },
    {
        'email': 'blaa@blaa.com',
        'plaintext_password': '1',
        'firstName': 'Петя',
        'lastName': 'Васильев',
        'city': 'Омск',
        'path': 'images/users/3.jpg'
    },
    {
        'email': 'admin@admin.ru',
        'plaintext_password': 'admin',
        'lastName': 'Администратор',
        'firstName': 'Администратор',
        'city': 'Санкт-Петербург',
        'path': 'images/users/admin.jpg'
    },

]

db.drop_all()
db.create_all()

for user_profile in users_profiles:
    db.session.add(UserProfile(user_profile))

db.session.commit()
