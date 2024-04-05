from django import forms
from .models import Review, Comic, Book, Category, Subcategory
from .widgets import CustomClearableFileInput


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['class'] = 'review-form-body'

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if not body.strip():
            raise forms.ValidationError("Body cannot be empty.")
        elif len(body) > 500:
            raise forms.ValidationError("Body cannot exceed 500 characters.")
        return body


class AddComicForm(forms.ModelForm):
    """A form to add a comic book"""

    class Meta:
        model = Comic
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Source: Boutique Ado walktrough project
        categories = Category.objects.filter(product_type='comic')
        # categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields['category'].choices = [('', '---------')] + display_names

        subcategories = Subcategory.objects.filter(
            category__product_type='comic')
        self.fields['subcategory'].queryset = subcategories


class AddBookForm(forms.ModelForm):
    """A form to add a book"""

    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Source: Boutique Ado walktrough project
        categories = Category.objects.filter(product_type='book')
        # categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields['category'].choices = [('', '---------')] + display_names

        subcategories = Subcategory.objects.filter(
            category__product_type='book')
        self.fields['subcategory'].queryset = subcategories
