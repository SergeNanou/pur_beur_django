
# coding: utf-8
import django
django.setup()
import requests
import regex as re

from django.db import models
from research.models import Product, Category





search = ['pizza', 'viennoiseries', 'Snacks', 'Epicerie', 'Desserts', 'Boissons',
          'Viandes','Poissons', 'Conserves', 'Biscuits' ]

	
for search_term in search:
	c = Category(name=search_term)
	c.save()
		
	payload = {"search_terms": search_term,"search_tag": 
                   "categories","page_size": 1000, "json": 1}
	res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", 
                            params=payload)
	# url result 
	res.url
	liste_store = []
	# result of json request 
	results = res.json()
	products = results["products"]
		# selection data  type 
	for product in products:
	# test to ensure the our attributs presence 
		if 'nutrition_grade_fr' in product.keys() and  'product_name_fr' in product.keys() and  'stores' in product.keys() and 'image_front_url'in product.keys() and 'nutriments' in product.keys() and 'nutrient_levels' in product.keys():
			if 'url' in product.keys() and 'code' in product.keys() and 'ingredients_text_fr' in product.keys() and  'stores' in product.keys() and 'nutrition_score_debug' in product.keys():
				store = product['stores']
				code = product['code']
				nutri = product['nutrition_grade_fr']
				nutri = re.sub(r"\p{P}+", r"", nutri)
				prod = product['product_name_fr']
				nutri_100 = product['nutrition_score_debug']
				# regex to delete punctuation in data
				prod =  re.sub(r"\p{P}+", r"", prod) 
				url = product['url']
				ingred = product['ingredients_text_fr']
				ingred = re.sub(r"\p{P}+", r"", ingred)
				nutriments = product['nutriments']
				# nutriments = re.sub(r"\p{P}+", r"", nutriments)
				nutrient_levels = product['nutrient_levels']
				# nutrient_levels = re.sub(r"\p{P}+", r"", nutrient_levels)

				# nutri_1.save()
				# url_1 = Product(url=url)
				# url_1.save()
				# ingred_1 = Product(description=ingred)
				# ingred_1.save()
				# prod_1 = Product(name_product=prod)
				# prod_1.save()
				image_url = product['image_front_url']
				
				p = Product(nutrition_score=nutri,url=url,
					        description=ingred,name_product=prod, 
					        nutrition_100=nutri_100,
					        nutriments=nutriments, 
					        nutrient_levels= nutrient_levels,
					        image=image_url)
				
				p.save()
	
				p.category.add(c)
				
					
