from django import forms
from .models import Review, Comic, Book, Category, Subcategory


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class AddComicForm(forms.ModelForm):
    """A form to add a comic book"""

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     categories = Category.objects.all()
        # for category in categories:
        #     subcategories = Subcategory.objects.filter(category=category)
        #     choices = [(subcategory.id, subcategory.name) for subcategory in subcategories]
        #     self.fields[f'subcategory_{category.id}'] = forms.ChoiceField(label=f'Subcategory for {category.name}', choices=choices, required=False)

    class Meta:
        model = Comic
        fields = '__all__'


class AddBookForm(forms.ModelForm):
    """A form to add a book"""

    class Meta:
        model = Book
        fields = '__all__'


class SubcategoryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        super().__init__(*args, **kwargs)
        self.fields['subcategory'] = forms.ChoiceField(choices=choices)