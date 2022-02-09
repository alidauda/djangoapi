from django.contrib import admin
from . models import Product, Users
# Register your models here.
admin.site.register(Users)
admin.site.register(Product)