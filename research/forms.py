from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Produit', 
                    widget=forms.TextInput(attrs={'class':'query','id': 'query', 'placeholder': 'Rechercher'}))