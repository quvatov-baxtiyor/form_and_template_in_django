from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import BookForm
from .models import Book


# from django.http import HttpResponse

# Create your views here.
class HelloWorld(TemplateView):

    def get(self, request):
        name = request.GET.get('name', 'World')
        # return HttpResponse(f"Hello, {name}")
        return render(
            request, 'library/home.html', {'name': name}
        )


def book_list(request):
    search = request.GET.get('search')
    if search is None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(title__icontains=search)

    return render(request, 'library/books.html', {'books': books, 'search': search})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'library/book.html', {'book': book})


def book_create(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            book = Book.objects.create(title=data['title'], author=data['author'], count=data['count'],)
            return redirect("books_view")
    return render(request, 'library/book_create.html', {'form': form})
