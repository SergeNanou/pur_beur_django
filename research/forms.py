from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(label='Produit', 
                    widget=forms.TextInput(attrs={'placeholder': 'Rechercher','id': 'query'}))