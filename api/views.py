from pickle import FALSE
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, UserSerializer
from .models import Users
# Create your views here.


@api_view(['GET'])
def getUser(request):

    user = Users.objects.all()
    serializer = UserSerializer(user, many=True)
    items={
            "user":serializer.data
        }
    return Response(items)


@api_view(['POST'])
def createUser(request):
    try:
        data = request.data
        createUser = Users.objects.create(
            shopname=data['shopname'],
            email=data['email']
        )
        serializer = UserSerializer(createUser, many=False)
        items={
            "user":serializer.data
        }
        return Response(serializer.data)
    except IntegrityError:
        content={'error':"user already exist "}
        error={"error":content}
        return Response(error)


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
