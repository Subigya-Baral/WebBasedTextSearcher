from django import forms

class SearchText(forms.Form):
    your_name = forms.CharField(label='Search Directory: ', max_length=100)
