from django.contrib import admin
from django.urls import path
from Product import views

urlpatterns = [
    path('profilepage/',views.shopping,name="shopping"),
    path('catagory/',views.product_catagory,name="catagory"),
    path('filter/<slug:slug>/',views.sub_catagory,name="sub-catagory"),
    path('search/',views.search_product,name="search"),
    path('cartsuccessfull/',views.add_to_cart,name="add-to-cart"),
    path('cartproduct/',views.cart_product,name="cart-product"),
    path('increaseitem/',views.increse_cart_item,name="add-item"),
    path('decreseitem/',views.decrese_cart_item,name="sub-item"),
    path('removeproduct/<int:id>/',views.remove_item,name="remove-cart-item"),
    path('productcard/<int:id>/',views.single_product,name="product-card"),
    path('selectaddress/',views.addres_selection,name="select-address"),
    path('orderaddress/',views.order_address,name="order-address"),
    path('placeorder/',views.placeorder,name="place-order"),
]