from django import forms


def validate_message_length(value):
    if len(value) > 1000:
        raise forms.ValidationError('The message must be no more than 500 characters.')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, validators=[validate_message_length])

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'message': 'Your message (max 1000 characters)',
        }
        classes = {
            'name': 'form-control',
            'email': 'form-control',
            'message': 'form-control',
        }
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].widget.attrs['class'] = classes[field]
            self.fields[field].label = False
        self.fields['name'].widget.attrs['autofocus'] = True
    
    def clean_name(self):
        """
        Clean the name field and remove leading and trailing whitespace
        """
        name = self.cleaned_data['name'].strip()
        return name

    def clean_email(self):
        """
        Clean the email field and remove leading and trailing whitespace
        """
        email = self.cleaned_data['email'].strip()
        return email

    def clean_message(self):
        """
        Clean the message field and remove leading and trailing whitespace
        """
        message = self.cleaned_data['message'].strip()
        return message
