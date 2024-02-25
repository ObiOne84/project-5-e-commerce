from django import forms
from .models import Review, Comic, Book, Category, Subcategory


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class AddComicForm(forms.ModelForm):
    """A form to add a comic book"""

    class Meta:
        model = Comic
        fields = '__all__'

