from rest_framework.serializers import ModelSerializer
from .models import Product, Users


class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields=["id","shopname","email","created_at","updated_at"]
    

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'
