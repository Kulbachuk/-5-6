from django import forms
from django.core.exceptions import ValidationError

CATEGORY_CHOICES = [
    ('programming', 'Програмування'),
    ('cybersecurity', 'Кібербезпека'),
    ('devops', 'DevOps & Мережі'),
]

class BookForm(forms.Form):
    title = forms.CharField(
        label='Назва книги',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email автора / читача',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    category = forms.ChoiceField(
        label='Категорія',
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        label='Опис книги',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        words = description.split()
        if len(words) < 3:
            raise ValidationError('Опис повинен містити принаймні 3 слова!')
        return description