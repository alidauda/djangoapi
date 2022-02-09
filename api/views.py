from pickle import FALSE
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, UserSerializer
from .models import Users
# Create your views here.


@api_view(['GET'])
def getUser(request, pk):

    user = Users.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createUser(request):
    data = request.data
    createUser = Users.objects.create(
        shopname=data['shopname'],
        email=data['email']
    )
    serializer = UserSerializer(createUser, many=False)
    return Response(serializer.data)


@api_view(['GET','POST'])
def getProducts(request, pk):
    if request.method == 'GET':
        user = Users.objects.get(id=pk)
        products = user.product_set.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        data = request.data
        user = Users.objects.get(id=pk)
        products = user.product_set.create(
            productName=data['productName'], price=data['price'], quantity=data['quantity'])

        serializer = ProductSerializer(products, many=False)
        return Response(serializer.data)
