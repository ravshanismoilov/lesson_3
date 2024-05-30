from django.shortcuts import render, redirect
from .models import Category, Author, Language, Books


def homepage(request):
    return render(request, 'index.html')


def get_category(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories': categories
    }
    return render(request, 'books/category.html', context=context)


def get_category_detail(request, pk):
    types = Books.objects.filter(pk=pk).order_by('-id')
    context = {
        'types': types
    }
    return render(request, 'books/category_detail.html', context=context)