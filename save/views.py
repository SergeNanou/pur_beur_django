import regex as re
import ast
from django.shortcuts import render
from save.models import Product_subs
from research.forms import SearchForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.

form = SearchForm()
save = []
@login_required(login_url='/index/')
def save_prod(request):

    current_user = request.user
    if request.method == "POST":

        query = request.POST['subs_0']
        query = query.split("+")
        
        Product_subs.objects.update_or_create(name_product=query[1],
                                              name_product_subs=query[0],
                                              image_product_subs=query[3],
                                              prod_sub_nut=query[4],
                                              nut_100=query[5],
                                              cuurent_user=current_user.id,
                                              url_subs=query[6],
                                              nut_levels=query[7],
                                              image_product=query[2])
    save = list(Product_subs.objects.filter(cuurent_user=current_user.id).values())
    # Slice pages
    paginator = Paginator(save, 2)
    # Get current page number
    page = request.GET.get('page')
    try:
        # Return only this page albums and not others
        save = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        save = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        save = paginator.page(paginator.num_pages)
            
        
    context_1 = {'form':form,'save': save}
          
        
    return render(request,'save/ind_pge_favorite.html',
                  context_1)
    
       
q_lip_fr = ''
q_lip_1 = ''
q_sat_fr = ''
q_sat_1 = ''
q_sugar_fr = ''
q_sugar_1 = ''
q_sodium_fr = ''
q_sodium_1 = ''
context = {}
@login_required(login_url='/index/')
def aliment(request):
    
    
    if request.method == "POST":
        query_1 = request.POST['subs_1']
        query_1 = query_1.split('+')

        a = ast.literal_eval(query_1[1])
        a_1 = ast.literal_eval(query_1[4])
        query_lip = a['fat_100g']
            
        q_lip_fr = a_1['fat']
        if q_lip_fr == 'low':
            q_lip_1 = 'en faible quantité'
        elif q_lip_fr == 'moderate':
            q_lip_1 = 'en quantité moyenne'
        elif q_lip_fr == 'high':
            q_lip_1 = 'en quantité élevée'
        
        query_sat = a['saturated-fat_100g']
        q_sat_fr = a_1['saturated-fat']
        if q_sat_fr == 'low':
            q_sat_1 = 'en faible quantité'
        elif q_sat_fr == 'moderate':
            q_sat_1 = 'en quantité moyenne'
        elif q_sat_fr == 'high':
            q_sat_1 = 'en quantité élevée'
            
        query_sugar = a['sugars_100g']
        q_sugar_fr = a_1['sugars']
        if q_sugar_fr == 'low':
            q_sugar_1 = 'en faible quantité'
        elif q_sugar_fr == 'moderate':
            q_sugar_1 = 'en quantité moyenne'
        elif q_sugar_fr == 'high':
            q_sugar_1 = 'en quantité élevée'
            
        query_sodium = a['salt']
        q_sodium_fr = a_1['salt']
        if q_sodium_fr == 'low':
            q_sodium_1 = 'en faible quantité'
        elif q_sodium_fr == 'moderate':
            q_sodium_1 = 'en quantité moyenne'
        elif q_sodium_fr == 'high':
            q_sodium_1 = 'en quantité élevée'
        context = {"nut": query_1[0], "sub_url": query_1[2],
                   "lip_0": query_lip, "lip": q_lip_fr,
                   "lip_1": q_lip_1, "sat_0": query_sat,
                   "sat": q_sat_fr, "sat_1": q_sat_1,
                   "sugar_0": query_sugar, "sugar": q_sugar_fr,
                   "sugar_1": q_sugar_1, "sodium_0": query_sodium,
                   "sodium": q_sodium_fr, "sodium_1":q_sodium_1,
                   "product": query_1[3], "image":query_1[5], "form":form}
        return render(request,'save/ind_pge_aliment.html',
                      context)



            

