from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Search Form Movies..', max_length=100)