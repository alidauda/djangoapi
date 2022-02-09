from django.db import models
import uuid
# Create your models here.
class Users(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shopname=models.CharField(unique=True, max_length=255)
    email=models.EmailField(unique=True, max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    password=models.CharField(max_length=255)


class Product(models.Model):
    owner=models.ForeignKey(Users,on_delete=models.CASCADE)
    productName=models.CharField(max_length=255)
    price=models.FloatField(max_length=255)
    quantity=models.IntegerField()
    product_ID=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    