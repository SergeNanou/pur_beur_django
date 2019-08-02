# coding: utf-8
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amateurs_nutella.settings")

def insert(self):
	# category types
	search = ['pizza', 'viennoiseries', 'Snacks', 'Epicerie', 'Desserts']
	# Openfoodfacts API request to take a data for category types
	for search_term in search:
		
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
			if 'nutrition_grade_fr' in product.keys() and  'product_name_fr' in product.keys() and  'stores' in product.keys() :
				if 'url' in product.keys() and 'code' in product.keys() and 'ingredients_text_fr' in product.keys() and  'stores' in product.keys():
					code = product['code']
					nutri = product['nutrition_grade_fr']
					prod = product['product_name_fr']
					# regex to delete punctuation in data
					prod =  re.sub(r"\p{P}+", r"", prod) 
					url = product['url']
					ingred = product['ingredients_text_fr']
					ingred = re.sub(r"\p{P}+", r"", ingred)
					store = product['stores']
					