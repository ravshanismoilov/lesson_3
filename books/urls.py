from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name='homepage'),
    path('category/', get_category, name='category'),
    path('category-detail/<int:pk>', get_category_detail, name='category-detail'),
]