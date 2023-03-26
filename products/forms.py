from django import forms
from .models import Comment


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'search for mobile'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'recommend', 'star']
