from django.contrib import admin

# Register your models here.

from research.models import *

admin.site.register(Product)
admin.site.register(Category)

