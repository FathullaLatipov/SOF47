from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired


# Форма для регистрации
class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired('Заполните имя!')])
    email = EmailField('Почта', validators=[DataRequired('Заполни EMAIL')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполни пароль')])
    confirm_password = PasswordField('Подтвержения пароля', validators=[DataRequired('Подвердите пароль!')])
    button = SubmitField('Зарегистрироваться')


# Форма для логина
class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired('Заполни EMAIL')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполни пароль')])

    button = SubmitField('Войти')
