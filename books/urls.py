from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name='homepage'),
    path('category/', get_category, name='category'),
    path('add/', create_book, name='add'),
    path('category-detail/<int:pk>', get_category_detail, name='category-detail'),
    path('book-detail/<int:pk>', get_book_detail, name='book-detail'),
    path('book-delete/<int:pk>', book_delete, name='book-delete'),
    path('book-update/<int:pk>', update_book, name='book-update'),
]