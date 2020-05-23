from django.urls import path
from . import views


urlpatterns = [
    path('product/<int:key>/', views.Product_Details),
    path('', views.Get_All_Products, name='work'),
    path('add_to_cart/<int:key>', views.Add_To_Cart, name='work'),
    path('delete_cart', views.RemoveCart, name='work'),
    path('registration', views.RegistartionFrom, name='work'),
    path('register_user', views.UserAdd, name='work'),
    path('cart', views.Cart, name='work'),



]
