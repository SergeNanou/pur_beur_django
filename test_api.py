#! /usr/bin/python3
# -*- coding: Utf-8 -*-

from django.test import TestCase

import requests
import regex as re
import unidecode

def search(search_term,pge_size):

	
    payload = {"search_terms": search_term,"search_tag": 
               "categories","page_size": pge_size, "json": 1}
    res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", 
                            params=payload)
	# result of json request 
    results = res.json()
    products = results["products"][0]['product_name_fr']
    return(products)


m_success = search("Biscuits",1)

def test_with_request_get_mock_success(monkeypatch):
    product = 'PRINCE Gout CHOCOLAT au Ble Complet'
    class MockResponse:
        def json(self):
            return({"products":[{"product_name_fr":'PRINCE Gout CHOCOLAT au Ble Complet'}]})

    def mock_requests_get_sucess_1(url,  params):
        return MockResponse()
    monkeypatch.setattr('requests.get', mock_requests_get_sucess_1)
    assert search("Biscuits",1) == product




# # selection data  type 
# for product in products:
# # test to ensure the our attributs presence 
# 	if 'nutrition_grade_fr' in product.keys() and  'product_name_fr' in product.keys() and  'stores' in product.keys() and 'image_front_url'in product.keys() and 'nutriments' in product.keys() and 'nutrient_levels' in product.keys():
# 		if 'url' in product.keys() and 'code' in product.keys() and 'ingredients_text_fr' in product.keys() and  'stores' in product.keys() and 'nutrition_score_debug' in product.keys():
# 			liste_store.append(product)
			
# 				# store = product['stores']
# 				# code = product['code']
# 				# nutri = product['nutrition_grade_fr']
# 				# nutri = re.sub(r"\p{P}+", r"", nutri)
# 				# prod = product['product_name_fr']
# 				# nutri_100 = product['nutrition_score_debug']
# 				# # regex to delete punctuation in data
# 				# prod =  re.sub(r"\p{P}+", r"", prod) 
# 				# url = product['url']
# 				# ingred = product['ingredients_text_fr']
# 				# ingred = re.sub(r"\p{P}+", r"", ingred)
# 				# nutriments = product['nutriments']
# 				# # nutriments = re.sub(r"\p{P}+", r"", nutriments)
# 				# nutrient_levels = product['nutrient_levels']
# 				# # nutrient_levels = re.sub(r"\p{P}+", r"", nutrient_levels)

# 				# # nutri_1.save()
# 				# # url_1 = Product(url=url)
# 				# # url_1.save()
# 				# # ingred_1 = Product(description=ingred)
# 				# # ingred_1.save()
# 				# # prod_1 = Product(name_product=prod)
# 				# # prod_1.save()
# 				# image_url = product['image_front_url']
# product = liste_store[0]
# prod = product['product_name_fr']
# prod =  re.sub(r"\p{P}+", r"", prod) 
# prod = unidecode.unidecode(prod)
# print(prod)

# # print(product['nutrition_grade_fr'])
# # print(product['nutrition_score_debug'])
# # print(product['ingredients_text_fr'])
# # print(product['nutrient_levels'])

# product = {"product_name_fr":"PRINCE Goût CHOCOLAT au Blé Complet",
#            'nutrition_grade_fr': 'd',
#            'nutrition_score_debug': '-- energy 5 + sat-fat 5 + \
#            fr-sat-fat-for-fats 4 + sugars 7 + sodium 2 \
#            - fruits 0% 0 - fiber 4 - proteins 3 -- fsa 15 -- fr 15',
#            'ingredients_text_fr':'Céréale 50,7 % (farine de \
#            blé 35 %, farine de blé complète 15,7 %), sucre, \
#            huiles végétales (palme, colza), cacao maigre en \
#            poudre 4,5 %, sirop de glucose, amidon de blé,\
#            poudre à lever (carbonate acide d''ammonium,\
#            carbonate acide de sodium, diphosphate disodique),\
#            émulsifiants (lécithine de soja, lécithine de \
#            tournesol), sel, lait écrémé en poudre, \
#            lactose et protéines de lait, arômes.',
#            'nutrient_levels': '{''saturated-fat''\
#            : ''high'', ''sugars'': ''high'', ''fat''\
#            : ''moderate'', ''salt'': ''moderate''}'}
