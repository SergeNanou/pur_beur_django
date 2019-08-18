from django.db import models


# Create model Product Substitut
class Product_subs(models.Model):
    name_product = models.CharField(max_length=1000)
    name_product_subs = models.CharField(max_length=1000)
    prod_sub_nut= models.CharField(max_length=1000)
    nut_100 = models.TextField()
    nut_levels = models.TextField()
    image_product = models.CharField(max_length=2000)
    image_product_subs = models.CharField(max_length=2000)
    cuurent_user = models.IntegerField()
    url_subs = models.CharField(max_length=2000)
    
    class Meta:
        verbose_name = "Product_subs"
    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.name_product,
                                             self.name_product_subs,
                                             self.image_product,
                                             self.image_product_subs,
        	                                 self.prod_sub_nut,
                                             self.nut_100,
                                             self.nut_levels)
