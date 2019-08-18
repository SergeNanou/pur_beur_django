from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from save.models import Product_subs


current_user = 0
class SavePageTestCase(TestCase):
    
    def setUp(self):
        self.credentials = {'username': 'testuser',
                            'password': 'secret',
                            'email': 'connect@yahoo.fr'}
        User.objects.create_user(**self.credentials)
        current_user = User.id
    def test_register(self):
        # send register data
        response = self.client.post('/register/',
                                    self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
    def test_login(self):
        # send login data
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        response = self.client.post('/user_login/',
                                    self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        
    
    def test_post_save(self):
        # set up test 
        response = self.client.post('/save/',
                                    {'subs_0': 'yaourt+yaourt_image\
                                    +a+url+100g+yaourrt_bio_image'})
        query = {'subs_0': 'yaourt+yaourt_bio+yaourt_image\
                 +a+salt-100g+url+100g+yaourrt_bio_image'}
        query = query['subs_0']
        query = query.split("+")
        Product_subs.objects.update_or_create(name_product=query[1],
                                              name_product_subs=query[0],
                                              image_product_subs=query[3],
                                              prod_sub_nut=query[4],
                                              nut_100=query[5],
                                              cuurent_user=current_user,
                                              url_subs=query[6],
                                              nut_levels=query[7],
                                              image_product=query[2])
        save = list(Product_subs.objects.filter(cuurent_user=current_user).values())
        # test  for page save
        response = self.client.get('/save/', {'save':save})
        self.assertEqual(response.status_code, 302)

        