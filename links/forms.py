
from django import forms

from links.models import Link


class LinkForm(forms.ModelForm):
    long_link = forms.URLField(max_length=250, widget=forms.URLInput(attrs={
        'id': 'long-link',
        'class': 'input'
    }))
    short_link = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id': 'short-link',
        'class': 'input'
    }))

    class Meta:
        model = Link
        fields = ('username', 'long_link', 'short_link')




