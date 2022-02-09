
from . import views
from django.urls import include, path

urlpatterns = [
   path('user/<str:pk>/', views.getUser, name='user'),
   path('newuser/', views.createUser, name='newuser'),
   path('product/<str:pk>/', views.getProducts, name='product'),
   
   
]
