
from research.forms import SearchForm
from research.models import Category
from research.models import Product
from django.db.models import Q

def algorythm(product):
    prod_list = []
    nutri = ''
  

    nutri = list(Product.objects.filter
               (name_product__contains=product)
               .values('nutrition_score'))[0]
    
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
    return(prod_list)
def algo_image(product):
    prod_image_0 = ''
    prod_image_0 = list(Product.objects.filter
                      (name_product__contains=product)
                      .values('image'))[0]
    prod_image_0 = prod_image_0['image']
    return(prod_image_0)
