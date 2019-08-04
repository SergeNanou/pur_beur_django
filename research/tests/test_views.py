
from django.test import TestCase
from research.forms import SearchForm
from django.contrib.auth.models import User
from research.models import Category
from research.models import Product


class SearchPageTestCase(TestCase):
    
    def test_post_search(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret',
            'email': 'connect@yahoo.fr'}
        User.objects.create_user(**self.credentials)
        p= Product.objects.create(name_product='yaourt bio', 
                                  description='100g de lait',
                                  nutriments='sugar-100',
                                  nutrient_levels='2g de sucre',
                                  nutrition_score='a',
                                  nutrition_100='b',
                                  image='https:// la belle_image')
        p_0= Product.objects.create(name_product='yaourt', 
                                  description='100g de lait',
                                  nutriments='sugar-100',
                                  nutrient_levels='2g de sucre',
                                  nutrition_score='b',
                                  nutrition_100='b',
                                  image='https:// la belle_image')

        c = Category.objects.create(name='desserts')
        p.category.add(c)
        p_0.category.add(c)
        
        response = self.client.post('/register/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        response = self.client.post('/user_login/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/search/', {'q': 'yaourt'})
        self.assertEqual(response.status_code, 200)
        
        form = SearchForm({'q': 'yaourt'})
        self.assertTrue(form.is_valid())
        product = form.cleaned_data['q']