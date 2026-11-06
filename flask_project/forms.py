from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

CATEGORY_CHOICES = [
    ('programming', 'Програмування'),
    ('cybersecurity', 'Кібербезпека'),
    ('devops', 'DevOps & Мережі'),
]

class BookForm(FlaskForm):
    title = StringField('Назва книги', validators=[
        DataRequired(message="Обов'язкове поле"),
        Length(max=100, message="Не більше 100 символів")
    ])
    email = StringField('Email автора / читача', validators=[
        DataRequired(message="Обов'язкове поле"),
        Email(message="Некоректний формат email")
    ])
    category = SelectField('Категорія', choices=CATEGORY_CHOICES)
    description = TextAreaField('Опис книги', validators=[
        DataRequired(message="Обов'язкове поле")
    ])
    submit = SubmitField('Зберегти')

    def validate_description(self, field):
        words = field.data.split()
        if len(words) < 3:
            raise ValidationError('Опис повинен містити принаймні 3 слова!')