from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from research.forms import SearchForm
from research.models import Category
from research.models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


# variable initiliazation 
prod_list = []
b = []
c = []
a_1 = 0
b_1 = 0
context_1 = {}
nutri = ''
product = ''
prod_image_0 = ''
form = SearchForm()
message = ''

# view for reception page
def reception(request):

    message = ''
    return render(request, 'search.html',
                  {'form': form, 'message': message})


@login_required(login_url='/index/')
def search(request):

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
                    nutri = list(Product.objects.filter
                                 (name_product__contains=product)
                                 .values('nutrition_score'))[0]
                    prod_image_0 = list(Product.objects.filter
                                        (name_product__contains=product)
                                        .values('image'))[0]
                    prod_image_0 = prod_image_0['image']
                    # prod_image_0 = '/media/'+ prod_image_0
                    c = list(Category.objects.filter
                             (cat_product__name_product__contains=product).
                             values('name'))[0]
                    if (nutri['nutrition_score'] == 'e' or
                        nutri['nutrition_score'] == 'd' or
                        nutri['nutrition_score'] == 'c'):
                        prod_list = list(Product.objects.filter
                                         (category__name=c['name']).
                                         filter(Q(nutrition_score='a')
                                         |Q(nutrition_score='b')).
                                         values().order_by('?'))
                    elif(nutri['nutrition_score'] == 'b'
                         or nutri['nutrition_score'] == 'a'):
                        prod_list = list(Product.objects.filter
                                          (category__name=c['name'],
                                          nutrition_score='a').values().
                                          order_by('?'))
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
