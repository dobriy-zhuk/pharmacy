from django.urls import path
from . import views


urlpatterns = [
    path('product/<str:name>/', views.Product_Details),
    path('', views.Get_All_Products, name='work'),
]
