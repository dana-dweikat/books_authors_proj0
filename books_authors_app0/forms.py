from django import forms

from .models import Book , Author


class BookForm(forms.ModelForm):
    class Meta:
        model= Book 
        fields = ["title", "description"]

    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'


class AuthorForm(forms.ModelForm):
    class Meta:
        model= Author 
        fields = ["first_name", "last_name","note"]

    
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['note'].widget.attrs['class'] = 'form-control'