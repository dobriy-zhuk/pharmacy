from django.urls import path
from . import views


urlpatterns = [
    path('product/<int:key>/', views.Product_Details),
    path('remove_from_cart/<int:key>/', views.DeleteFromCart),
    path('', views.Get_All_Products, name='work'),
    path('add_to_cart/<int:key>', views.Add_To_Cart, name='work'),
    path('delete_cart', views.RemoveCart, name='work'),
    path('registration', views.RegistartionFrom, name='work'),
    path('register_user', views.UserAdd, name='work'),
    path('login', views.login_form, name='login'),
    path('login_user', views.login_user, name='login_user'),
    path('cart', views.Cart, name='cart'),
    path('index', views.index, name='index'),
    path('new_cart', views.new_cart, name='index'),



]
