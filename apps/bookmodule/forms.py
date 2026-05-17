from django import forms
from .models import Book
from .models import Student
from .models import StudentImage

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'price']


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'addresses': forms.CheckboxSelectMultiple()
        }
