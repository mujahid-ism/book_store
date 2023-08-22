from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg

from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('-rating')
    return render(request, 'index.html', {
        'books': books,
        'number_of_books': len(books),
        'avg_rating': books.aggregate(Avg('rating'))
    })


def individual_book_detail(request, slug):
    # try:
    #     book = Book.objects.get(slug=slug)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_detail.html', {
        'book': book
    })
