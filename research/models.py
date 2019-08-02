from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Category"
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name_product = models.CharField(max_length=1000)
    description = models.TextField()
    nutriments = models.TextField()
    nutrient_levels = models.CharField(max_length=3000)
    url  = models.CharField(max_length=3000)
    nutrition_score = models.CharField(max_length=10)
    nutrition_100 = models.CharField(max_length=5000)
    category = models.ManyToManyField("Category", related_name="cat_product")
    image = models.CharField(max_length=3000)
    
    class Meta:
        verbose_name = "Product"
    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.name_product, self.description, 
                                          self.url, self.nutrition_score, 
                                          self.nutrition_100, self.nutriments,
                                          self.nutrient_levels, self.image )
# class Shop(models.Model):
#     name_shop = models.CharField(max_length=20)
#     def __str__(self):
#         return self.name_shop
#     class Meta:
#         verbose_name = "Shop"