from django.shortcuts import render
from django.contrib.auth.models import User
from research.algo import algorythm
from research.algo import algo_image
from research.forms import SearchForm
from research.models import Category
from research.models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


# variable initiliazation 

form = SearchForm()

# view for reception page
def reception(request):

    message = ''
    return render(request, 'search.html',
                  {'form': form, 'message': message})



def search(request):
    # variable initialization
    prod_list = []
    context_1 = {}
    nutri_0 = ''
    product = ''
    prod_image_0 = ''
    message = ''


    # Check if the session has already been created.
    # If created, get their values and store it.
    if not request.method == 'POST':
        if 'search-persons-post' in request.session:
            request.POST = request.session['search-persons-post']
            request.method = 'POST'
    # substitut algorithm
    if request.method == 'POST':
        form = SearchForm(request.POST)
        request.session['search-persons-post'] = request.POST
        if form.is_valid():
            product = form.cleaned_data['query']

            if product:

                nutri_0 = list(Product.objects.filter
                               (name_product__contains=product)
                               .values('nutrition_score'))
                if nutri_0:
                    prod_list = algorythm(product)
                    prod_image_0 = algo_image(product)
                    
                    # Slice pages
                    paginator = Paginator(prod_list, 6)
                    # Get current page number
                    page = request.GET.get('page')
                    try:
                        # Return only this page albums and not others
                        prod_list = paginator.page(page)
                    except PageNotAnInteger:
                        # If page is not an integer, deliver first page.
                        prod_list = paginator.page(1)
                    except EmptyPage:
                        # If page is out of range,
                        # deliver last page of results.
                        prod_list = paginator.page(paginator.num_pages)
                    context_1 = {'prod_list': prod_list, 'paginate': True,
                                 'prod_name_0': product,
                                 'form': form,
                                 'prod_image_0': prod_image_0}

                    return render(request, 'research/ind_pge_resultat.html',
                                  context_1)
                else:
                    form = SearchForm()
                    message = "Nous n'avons pas \
                               d'informations sur ce produit.\
                               Commencer par écrire les noms \
                               des produits en majuscules \
                               pour une meilleure utilisation \
                               de l'application.  \
                               Retourner et recharger \
                               à la page d'acceuil pour \
                               faire une nouvelle recherche "
                    return render(request, 
                                  'search.html',
                                  {'message': message})
        else:
            return render(request, 'search.html', {'form': form})
                                   
    else:
        return render(request, 'search.html', {'form': form})
