# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
    # max_length/ min_length
    title = forms.CharField(
        max_length=10,
        label="제목",
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title!',
            }
        )
    )
    content = forms.CharField(
        min_length=20, 
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content!',
                'row': 5,
                'cols': 50,
            }
        )
    )