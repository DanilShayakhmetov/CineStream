from flask_wtf import Form
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    firstName = StringField('Имя', validators=[DataRequired(), Length(min=1, max=50)])
    lastName = StringField('Фамилия', validators=[DataRequired(), Length(min=1, max=50)])
    city = StringField('Город')
    file = FileField('Фотография')


class LoginForm(Form):
    email = StringField('Электронная почта', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Пароль', validators=[DataRequired()])


class EditProfileForm(Form):
    email = StringField('Email')
    firstName = StringField('Имя')
    lastName = StringField('Фамилия')
    city = StringField('Город')
    file = FileField('Фотография')
