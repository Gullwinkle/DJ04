from .models import Movie
from django.forms import ModelForm, TextInput, Textarea

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'feedback']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название фильма'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание фильма'
            }),
            'feedback': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите отзыв'
            }),
        }