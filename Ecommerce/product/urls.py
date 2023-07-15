from django.urls import path
from product.views import *
from django.contrib import admin
from product import views
from django.conf.urls.static import static
from django.conf import settings
# from user import urls
urlpatterns = [
    path('catagory/',product_catagory,name="catagory"),
    path('filter/<slug:slug>/',sub_catagory,name="subcatagory"),
    path('getproduct/<int:id>', single_product,name="get-product"),
    path('cart/', views.add_to_cart, name='add-to-cart'),  
    path('showcart/', views.show_cart, name='show-cart'),  
    path('removeitem/<int:id>/', views.remove_item, name='remove-item'),
    path('add_product/',views.increse_cart_item,name="add-item"),
    path('remove_product/',views.decrese_cart_item,name="decrese-item"),
    path('placeorder/',views.place_order,name="place-order"),
    path('search/',views.search_product,name="search"),
    path('product-detail/',views.product_detail,name="product-detail"),
    path('selectaddress/',views.select_address,name="select-address"),
    path('order-address/',views.order_address,name="order-address"),
    path('debitcard/',views.debitcard,name="debit-card")

]