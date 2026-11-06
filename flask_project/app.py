from flask import Flask, render_template, redirect, url_for, flash
from flask_project.forms import BookForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask-super-secret-key-12345'

@app.route('/')
def home():
    items = ['Чистий код', 'Паттерни проектирования', 'Практична кібербезпека']
    context = {
        'title_page': 'Каталог IT-літератури (Flask)',
        'items_count': len(items),
        'featured_books': [
            {'title': 'Чистий код', 'author': 'Роберт Мартін', 'year': 2008},
            {'title': 'Паттерни проектирования', 'author': 'Еріх Гамма', 'year': 1994},
            {'title': 'Практична кібербезпека', 'author': 'Ендрю Таненбаум', 'year': 2021},
        ]
    }
    return render_template('home.html', **context)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        flash(f'Книгу "{form.title.data}" успішно додано до каталогу!', 'success')
        return redirect(url_for('home'))
    elif form.is_submitted():
        flash('Будь ласка, виправте помилки у формі.', 'error')
        
    return render_template('add_book.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5001)