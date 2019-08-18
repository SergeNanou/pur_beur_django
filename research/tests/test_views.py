
from django.test import TestCase
from research.forms import SearchForm
from django.contrib.auth.models import User
from research.models import Category
from research.models import Product

# test for research views product
class SearchPageTestCase(TestCase):

    def test_post_search(self):
        # setup for create user
        self.credentials = {'username': 'testuser',
                            'password': 'secret',
                            'email': 'connect@yahoo.fr'}
        User.objects.create_user(**self.credentials)
        # setup for create product
        p = Product.objects.create(name_product='yaourt bio', 
                                    description='100g de lait',
                                    nutriments='sugar-100',
                                    nutrient_levels='2g de sucre',
                                    nutrition_score='a',
                                    nutrition_100='b',
                                    image='https:// la belle_image')
        p_0 = Product.objects.create(name_product='yaourt',
                                     description='100g de lait',
                                     nutriments='sugar-100',
                                     nutrient_levels='2g de sucre',
                                     nutrition_score='b',
                                     nutrition_100='b',
                                     image='https:// la belle_image')
        # Add product at one category
        c = Category.objects.create(name='desserts')
        p.category.add(c)
        p_0.category.add(c)
        # Create user 
        response = self.client.post('/register/',
                                    self.credentials,
                                    follow=True)
        # test for page register
        self.assertEqual(response.status_code, 200)
        # Connect User
        self.credentials = {'username': 'testuser',
                            'password': 'secret'}
        # test for page connect
        response = self.client.post('/user_login/',
                                    self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/search/', {'query': 'yaourt'})
        self.assertEqual(response.status_code, 200)
        # test valid form
        form = SearchForm({'query': 'yaourt'})
        self.assertTrue(form.is_valid())
        product = form.cleaned_data['query']
