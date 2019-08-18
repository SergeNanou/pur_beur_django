from django import forms


class SearchForm(forms.Form):
    context = {'class':'query',
               'id': 'query', 
               'placeholder': 'Rechercher'}
    query = forms.CharField(label='Produit',
                            widget=forms.
                            TextInput(attrs=context))