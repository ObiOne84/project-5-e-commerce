from django import forms
from .models import Review, Comic, Book


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class AddComicForm(forms.ModelForm):
    """A form to add a comic book"""

    class Meta:
        model = Comic
        fields = '__all__'


class AddBookForm(forms.ModelForm):
    """A form to add a book"""

    class Meta:
        model = Book
        fields = '__all__'
