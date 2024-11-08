from django.shortcuts import *
from .models import Book, Author

def view_books(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def view_book(request, id):
    book = get_object_or_404(Book, id=id)
    authors = Author.objects.all()
    request.session['book'] = book.id
    return render(request, 'library.html', {'book': book, 'authors': authors})

def add_book(request):
    if request.method == 'POST':
        if len(request.POST['title']) < 1 or len(request.POST['desc']) < 1:
            return redirect('/')
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
        return redirect('/')
    return render(request, 'add_book.html')

def view_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

def view_author(request, id):
    author = get_object_or_404(Author, id=id)
    books = Book.objects.all()
    request.session['author'] = author.id
    return render(request, 'view_author.html', {'author': author, 'books': books})

def add_author(request):
    if request.method == 'POST':
        if len(request.POST['first_name']) < 1 or len(request.POST['last_name']) < 1 or len(request.POST['notes']) < 1:
            return redirect('/authors')
        Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
        return redirect('/authors')
    return render(request, 'add_author.html')

def assign_author(request):
    book_id = request.session.get('book')
    if book_id and request.POST.get('author') and request.POST['author'] != 'none':
        book = get_object_or_404(Book, id=book_id)
        author = get_object_or_404(Author, id=request.POST['author'])
        book.add_author(author)
    return redirect(f'/library/{book_id}')

def assign_book(request):
    author_id = request.session.get('author')
    if author_id and request.POST.get('book') and request.POST['book'] != 'none':
        author = get_object_or_404(Author, id=author_id)
        book = get_object_or_404(Book, id=request.POST['book'])
        author.add_book(book)
    return redirect(f'/view_author/{author_id}')
