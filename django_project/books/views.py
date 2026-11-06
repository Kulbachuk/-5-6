from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookForm

# Головна сторінка з контекстом
def home(request):
    context = {
        'title_page': 'Каталог IT-літератури',
        'items_count': 3,
        'featured_books': [
            {'title': 'Чистий код', 'author': 'Роберт Мартін', 'year': 2008},
            {'title': 'Паттерни проектування', 'author': 'Еріх Гамма', 'year': 1994},
            {'title': 'Практична кібербезпека', 'author': 'Ендрю Таненбаум', 'year': 2021},
        ]
    }
    return render(request, 'books/home.html', context)

# Сторінка додавання книги
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            messages.success(request, f'Книгу "{title}" успішно додано до каталогу!')
            return redirect('home')
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = BookForm()

    return render(request, 'books/add_book.html', {'form': form})