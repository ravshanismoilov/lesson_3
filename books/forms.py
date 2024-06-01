from .models import Books
from django.forms import ModelForm


class CreateBookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'