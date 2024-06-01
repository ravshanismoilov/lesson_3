from django.shortcuts import render, redirect
from .models import Category, Author, Language, Books
from .forms import CreateBookForm
from django.views import View


def homepage(request):
    return render(request, 'index.html')


def get_category(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories': categories
    }
    return render(request, 'books/category.html', context=context)


def get_category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    types = Books.objects.filter(category=pk).order_by('-id')
    context = {
        'types': types,
        'category': category
    }
    return render(request, 'books/category_detail.html', context=context)


def get_book_detail(request, pk):
    book = Books.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'books/book_detail.html', context=context)


def book_delete(request, pk):
    book = Books.objects.get(pk=pk)
    context = {
        'book': book
    }
    if book:
        book.delete()
        return redirect('category-detail', pk=book.category_id)
    return render(request, 'books/book_delete.html', context=context)


def create_book(request):
    create_form = CreateBookForm(data=request.POST, files=request.FILES)
    if request.method == 'POST':
        if create_form.is_valid():
            create_form.save()
            return redirect('category')
    context = {
        'create_form': create_form
    }
    return render(request, 'books/create_book.html', context=context)


def update_book(request, pk):
    book = Books.objects.get(pk=pk)
    update_form = CreateBookForm(data=request.POST, files=request.FILES, instance=book)
    if request.method == 'POST':
        if update_form.is_valid():
            update_form.save()
            return redirect('book-detail', book.pk)
    context = {'update_form': update_form, 'book': book}
    return render(request, 'books/update_book.html', context=context)



