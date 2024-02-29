from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired


# Форма для регистрации
class CommentForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired('Заполните имя!')])
    title = StringField('Тема', validators=[DataRequired('Заполни тему')])
    comment = TextAreaField('Коммент', validators=[DataRequired('Заполни коммент')])
    button = SubmitField('Отправить коммент')